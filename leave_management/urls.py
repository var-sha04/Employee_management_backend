from django.urls import path
from .views import (
    LeaveListCreateAPIView,
    MyLeaveAPIView,
    LeaveListAPIView,
    LeaveRetrieveUpdateAPIView,

    
)

urlpatterns = [
    path(
        "leaves/",
        LeaveListCreateAPIView.as_view()
    ),
    path(
    "leaves/my/",
    MyLeaveAPIView.as_view()
    ),
    path(
    "leaves/all/",
    LeaveListAPIView.as_view()
    ),
    path(
    "leaves/<int:pk>/",
    LeaveRetrieveUpdateAPIView.as_view()
    ),
]