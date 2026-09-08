from django.urls import path

from .views import RegisterAPIView, AdminRegisterAPIView,RoleUpdateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin-register/",AdminRegisterAPIView.as_view(),name="admin-register"),
    path("users/<int:pk>/role/",RoleUpdateAPIView.as_view(),name="role-update"),
    
]