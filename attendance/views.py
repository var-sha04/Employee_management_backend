from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Attendance
from .serializers import AttendanceSerializer
from accounts.permissions import IsAdminOrHRForWrite
from accounts.permissions import IsAdminHROrOwnAttendance
from django.utils import timezone
from employees.models import Employee

class AttendanceListCreateAPIView(APIView):

    permission_classes = [IsAdminOrHRForWrite]

    def get(self, request):
        attendance = Attendance.objects.all()

        serializer = AttendanceSerializer(
            attendance,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = AttendanceSerializer(
            data=request.data
        )

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

class AttendanceRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAdminHROrOwnAttendance]

    def get_object(self, pk):
        try:
            return Attendance.objects.get(pk=pk)
        except Attendance.DoesNotExist:
            return None

    def get(self, request, pk):
        attendance = self.get_object(pk)

        if attendance is None:
            return Response(
                {"error": "Attendance record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, attendance)

        serializer = AttendanceSerializer(attendance)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        attendance = self.get_object(pk)

        if attendance is None:
            return Response(
                {"error": "Attendance record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, attendance)

        serializer = AttendanceSerializer(
            attendance,
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
        attendance = self.get_object(pk)

        if attendance is None:
            return Response(
                {"error": "Attendance record not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        self.check_object_permissions(request, attendance)

        serializer = AttendanceSerializer(
            attendance,
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

        attendance = self.get_object(pk)

        if attendance is None:
            return Response(
                {"error": "Attendance record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.user.profile.role != "ADMIN":
            return Response(
                {"detail": "Only admin can delete attendance."},
                status=status.HTTP_403_FORBIDDEN
            )

        attendance.delete()

        return Response(
            {"message": "Attendance deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

class AttendanceCheckInAPIView(APIView):

    permission_classes = [IsAdminHROrOwnAttendance]

    def post(self, request):

        if request.user.profile.role != "EMPLOYEE":
            return Response(
                {"error": "Only employees can check in."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            employee = request.user.employee
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        today = timezone.localdate()

        attendance = Attendance.objects.filter(
            employee=employee,
            date=today
        ).first()

        if attendance:
            return Response(
                {"error": "Attendance already marked for today."},
                status=status.HTTP_400_BAD_REQUEST
            )

        attendance = Attendance.objects.create(
            employee=employee,
            date=today,
            check_in=timezone.localtime().time(),
            status="PRESENT"
        )

        serializer = AttendanceSerializer(attendance)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

class AttendanceCheckOutAPIView(APIView):

    permission_classes = [IsAdminHROrOwnAttendance]

    def post(self, request):

        if request.user.profile.role != "EMPLOYEE":
            return Response(
                {"error": "Only employees can check out."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            employee = request.user.employee
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        today = timezone.localdate()

        attendance = Attendance.objects.filter(
            employee=employee,
            date=today
        ).first()

        if attendance is None:
            return Response(
                {"error": "Please check in first."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if attendance.check_out is not None:
            return Response(
                {"error": "Already checked out for today."},
                status=status.HTTP_400_BAD_REQUEST
            )

        attendance.check_out = timezone.localtime().time()
        attendance.save()

        serializer = AttendanceSerializer(attendance)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class MyAttendanceAPIView(APIView):

    permission_classes = [IsAdminHROrOwnAttendance]

    def get(self, request):

        if request.user.profile.role != "EMPLOYEE":
            return Response(
                {"error": "This endpoint is for employees."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            employee = request.user.employee
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        attendance = Attendance.objects.filter(
            employee=employee
        ).order_by("-date")

        serializer = AttendanceSerializer(
            attendance,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )