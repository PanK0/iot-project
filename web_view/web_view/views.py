# views for web_view

from django.shortcuts import render
from django.http import HttpResponse

def home(request) :
    return HttpResponse('<h1> Web View Home </h1>')
