from django.shortcuts import render,HttpResponse
from django.urls import *

# Create your views here.

def new11(request):
    return render(request,'new11.html')

def new2(request):
    return render(request,'new2.html')