from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.profile.role == "ADMIN"
        )

class IsAdminOrHRForWrite(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        # DELETE is ADMIN only
        if request.method == "DELETE":
            return request.user.profile.role == "ADMIN"

        # GET, POST, PUT, PATCH are ADMIN or HR
        return request.user.profile.role in ["ADMIN", "HR"]


class IsAdminHROrOwnAttendance(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        role = request.user.profile.role

        # Admin and HR can access attendance management
        if role in ["ADMIN", "HR"]:
            return True

        # Normal employees are allowed to use the attendance API
        if role == "EMPLOYEE":
            return True

        return False

    def has_object_permission(self, request, view, obj):

        role = request.user.profile.role

        # Admin and HR can access any attendance record
        if role in ["ADMIN", "HR"]:
            return True

        # Employee can access only their own attendance
        if role == "EMPLOYEE":
            return obj.employee.user == request.user

        return False