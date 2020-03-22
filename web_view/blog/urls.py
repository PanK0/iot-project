# Blog URLs

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),                 # blog home page
    path('about/', views.about, name='blog-about'),         # blog about page
]
