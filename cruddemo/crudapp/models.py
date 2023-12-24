from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=20)
    stu_rollno=models.IntegerField()
    stu_address=models.CharField(max_length=50)