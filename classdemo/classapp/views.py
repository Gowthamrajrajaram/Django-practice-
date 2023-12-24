from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

class Firstview(View):
    def get(self,request):
        return HttpResponse('<h1>Hello Everyone<h1>')