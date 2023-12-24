from django.shortcuts import render,redirect
from crudapp.models import Student
from crudapp.forms import studentform
# Create your views here.
def display(request):
    students=Student.objects.all()
    return render(request, 'app/crud.html', {'student':students})

def create(request):
    form=studentform()
    if request.method =='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'app/create.html',{'form':form})

def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/check')

def update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = studentform(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'app/update.html',{'student':student})

