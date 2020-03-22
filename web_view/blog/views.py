# views for blog

from django.shortcuts import render
from django.http import HttpResponse

def home(request) :
    return HttpResponse('<h1> Blog Home </h1>')

def about(request) :
    return HttpResponse('<h1> Bloh About </h1>')
