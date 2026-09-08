from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", lambda request: HttpResponse("Config URL works")),
    path("api/", include("employees.urls")),
    path("api/auth/", include("accounts.urls")),
    path("api/", include("attendance.urls")),
    path("api/", include("leave_management.urls")),

]