# views for web_view

from django.shortcuts import render
from django.http import HttpResponse

def home(request) :
    return render(request, 'web_view/home.html')

def assig1(request) :
    return render(request, 'web_view/assig1.html')

def assig2(request) :
    return render(request, 'web_view/assig2.html')

def assig3(request) :
    return render(request, 'web_view/assig3.html')
