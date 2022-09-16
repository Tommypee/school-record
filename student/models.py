from django.db import models
from department.models import Department

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    regno = models.CharField(max_length=6, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

