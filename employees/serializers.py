from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Department, Employee
from accounts.models import UserProfile
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "username",
            "password",
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "designation",
            "department",
            "user",
            "joining_date",
        ]
        read_only_fields = ["id", "user"]

    def create(self, validated_data):
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=validated_data.get("email", "")
        )

        UserProfile.objects.create(
            user=user,
            role="EMPLOYEE"
        )

        employee = Employee.objects.create(
            user=user,
            **validated_data
        )

        return employee