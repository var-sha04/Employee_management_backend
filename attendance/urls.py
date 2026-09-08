from django.urls import path
from .views import (
    AttendanceListCreateAPIView,
    AttendanceRetrieveUpdateDeleteAPIView,
    AttendanceCheckInAPIView,
    AttendanceCheckOutAPIView,
    MyAttendanceAPIView,


)

urlpatterns = [
    path(
        "attendance/",
        AttendanceListCreateAPIView.as_view()
    ),

    path(
        "attendance/<int:pk>/",
        AttendanceRetrieveUpdateDeleteAPIView.as_view()
    ),
    path(
    "attendance/check-in/",
    AttendanceCheckInAPIView.as_view()
    ),
    path(
    "attendance/check-out/",
    AttendanceCheckOutAPIView.as_view()
    ),
    path(
    "attendance/my/",
    MyAttendanceAPIView.as_view()
    ),
]