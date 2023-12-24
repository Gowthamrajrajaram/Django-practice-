from django.contrib import admin
from crudapp.models import Student
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list=['stu_name','stu_rollno','stu_address']

admin.site.register(Student,studentadmin)