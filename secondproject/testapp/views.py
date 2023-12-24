from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admins(request):
    return HttpResponse('<h1>admins name Gowtham</h1>')

def user1(request):
    return HttpResponse('<h1>user1 name manoj</h1>')

def user2(request):
    return HttpResponse('<h1>user2 name Guna</h1>')

def user3(request):
    return HttpResponse('<h1>user3 name kavin</h1>')