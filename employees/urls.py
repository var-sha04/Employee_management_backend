from django.urls import path
from .views import (
    DepartmentListCreateAPIView,
    DepartmentRetrieveUpdateDeleteAPIView,
    EmployeeListCreateAPIView,
    EmployeeRetrieveUpdateDeleteAPIView,

)

urlpatterns = [
    path(
        "departments/",
        DepartmentListCreateAPIView.as_view(),
        name="department-list-create",
    ),

    path(
        "departments/<int:pk>/",
        DepartmentRetrieveUpdateDeleteAPIView.as_view(),
        name="department-detail",
    ),

    path(
        "employees/",
        EmployeeListCreateAPIView.as_view(),
        name="employee-list-create",
    ),

    path(
    "employees/<int:pk>/",
    EmployeeRetrieveUpdateDeleteAPIView.as_view()
    ),
]