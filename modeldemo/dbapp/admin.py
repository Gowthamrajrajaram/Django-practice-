from django.contrib import admin
from dbapp.models import employes
# Register your models here.

class Employeadmin(admin.ModelAdmin):
    emp_list=["empno","emoname","empaddress","empsalary"]

admin.site.register(employes, Employeadmin)
