from accounts.permissions import IsAdmin
from accounts.permissions import IsAdminOrHRForWrite
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListCreateAPIView(APIView):
    permission_classes = [IsAdminOrHRForWrite]
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


class DepartmentRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAdminOrHRForWrite]
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return None
        
    def get(self, request, pk):
        department = self.get_object(pk)

        if department is None:
            return Response(
                {"error": "Department not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        department = self.get_object(pk)

        if department is None:
            return Response(
                {"error": "Department not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DepartmentSerializer(
            department,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        department = self.get_object(pk)

        if department is None:
            return Response(
                {"error": "Department not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DepartmentSerializer(
            department,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        department = self.get_object(pk)

        if department is None:
            return Response(
                {"error": "Department not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        department.delete()

        return Response(
            {"message": "Department deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

class EmployeeListCreateAPIView(APIView):

    permission_classes = [IsAdminOrHRForWrite]

    def get(self, request):

        employees = Employee.objects.all()

        search = request.query_params.get("search")
        department = request.query_params.get("department")
        department_id = request.query_params.get("department_id")       
        designation = request.query_params.get("designation")
        employee_id = request.query_params.get("employee_id")
        email = request.query_params.get("email")

        if search:
            employees = employees.filter(
                first_name__icontains=search
            ) | employees.filter(
                last_name__icontains=search
            )

        if department:
            employees = employees.filter(
                department__department_name__icontains=department
            )
        if department_id:
            employees = employees.filter(
                department_id=department_id
            )
        if designation:
            employees = employees.filter(
                designation__icontains=designation
            )

        if employee_id:
            employees = employees.filter(
                employee_id__icontains=employee_id
            )

        if email:
            employees = employees.filter(
                email__icontains=email
            )

        serializer = EmployeeSerializer(employees, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class EmployeeRetrieveUpdateDeleteAPIView(APIView):

    permission_classes = [IsAdminOrHRForWrite]

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None

    def get(self, request, pk):
        employee = self.get_object(pk)

        if employee is None:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployeeSerializer(employee)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        employee = self.get_object(pk)

        if employee is None:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployeeSerializer(
            employee,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        employee = self.get_object(pk)

        if employee is None:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployeeSerializer(
            employee,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        employee = self.get_object(pk)

        if employee is None:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        employee.delete()

        return Response(
            {"message": "Employee deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )       
print("Views imported successfully")