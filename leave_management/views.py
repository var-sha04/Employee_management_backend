from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Leave
from .serializers import LeaveSerializer


class LeaveListCreateAPIView(APIView):

    def post(self, request):

        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if request.user.profile.role not in ["ADMIN", "HR", "EMPLOYEE"]:
            return Response(
                {"error": "You do not have permission to apply for leave."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            employee = request.user.employee
        except Exception:
            return Response(
                {"error": "Employee profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = LeaveSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                employee=employee,
                status="PENDING"
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class MyLeaveAPIView(APIView):

    def get(self, request):

        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if request.user.profile.role not in ["ADMIN", "HR", "EMPLOYEE"]:
            return Response(
                {"error": "You do not have permission to view leave requests."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            employee = request.user.employee
        except Exception:
            return Response(
                {"error": "Employee profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        leaves = Leave.objects.filter(
            employee=employee
        ).order_by("-applied_at")

        serializer = LeaveSerializer(
            leaves,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class LeaveListAPIView(APIView):

    def get(self, request):

        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        role = request.user.profile.role

        if role not in ["ADMIN", "HR"]:
            return Response(
                {"error": "Only Admin or HR can view all leave requests."},
                status=status.HTTP_403_FORBIDDEN
            )

        leaves = Leave.objects.all()

        # Filter by status
        leave_status = request.query_params.get("status")

        if leave_status:
            leaves = leaves.filter(status=leave_status.upper())

        # Filter by leave type
        leave_type = request.query_params.get("leave_type")

        if leave_type:
            leaves = leaves.filter(leave_type=leave_type.upper())

        # Filter by employee ID
        employee_id = request.query_params.get("employee")

        if employee_id:
            leaves = leaves.filter(employee_id=employee_id)

        # Newest requests first
        leaves = leaves.order_by("-applied_at")

        serializer = LeaveSerializer(
            leaves,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
class LeaveRetrieveUpdateAPIView(APIView):

    def get_object(self, pk):
        try:
            return Leave.objects.get(pk=pk)
        except Leave.DoesNotExist:
            return None

    def get(self, request, pk):

        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        leave = self.get_object(pk)

        if leave is None:
            return Response(
                {"error": "Leave request not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        role = request.user.profile.role

        # Admin and HR can view any leave request
        if role in ["ADMIN", "HR"]:
            serializer = LeaveSerializer(leave)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        # Employee can view only their own leave
        if role == "EMPLOYEE":

            if leave.employee.user != request.user:
                return Response(
                    {"error": "You can only view your own leave requests."},
                    status=status.HTTP_403_FORBIDDEN
                )

            serializer = LeaveSerializer(leave)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            {"error": "You do not have permission to view this leave request."},
            status=status.HTTP_403_FORBIDDEN
        )

    def patch(self, request, pk):

        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        leave = self.get_object(pk)

        if leave is None:
            return Response(
                {"error": "Leave request not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        role = request.user.profile.role

        # Only Admin and HR can approve/reject
        if role not in ["ADMIN", "HR"]:
            return Response(
                {"error": "Only Admin or HR can update leave status."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Don't allow changing an already processed leave
        if leave.status != "PENDING":
            return Response(
                {
                    "error": "This leave request has already been processed."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        new_status = request.data.get("status")

        if new_status not in ["APPROVED", "REJECTED"]:
            return Response(
                {
                    "error": "Status must be APPROVED or REJECTED."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        leave.status = new_status
        leave.save()

        serializer = LeaveSerializer(leave)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
# Create your views here.
