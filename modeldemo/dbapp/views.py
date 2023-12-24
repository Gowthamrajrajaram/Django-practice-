from django.shortcuts import render
from dbapp.models import employes
# Create your views here.

def empdetails(request):
    emp_data=employes.objects.all()
    emp_details={'emplist':emp_data}
    return render(request, 'app/DBapp.html', context=emp_details)
