import re
from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def detail(request):
    return render(request,'detail.html')


# Create your views here.
