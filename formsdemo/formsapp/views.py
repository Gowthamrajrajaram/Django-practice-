from django.shortcuts import render
from . import form

def employe(request):
    forms=form.employeinfoform()
    empinfo={'forms':forms}
    return render(request, 'app/form.html' ,context=empinfo)
