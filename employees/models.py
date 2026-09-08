from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    department_code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees"
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee",
        null=True,
        blank=True
    )
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"