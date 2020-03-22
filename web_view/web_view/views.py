# views for web_view

from django.shortcuts import render
from django.http import HttpResponse

def home(request) :
    return render(request, 'web_view/home.html')
