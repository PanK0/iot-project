# web_view URL Configuration

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),                    # admin panel route
    path('', views.home, name='web_view_home'),         # general home page
    path('blog/', include('blog.urls'), name='blog-home'),                # blog home page
    path('blog/about', include('blog.urls'), name='blog-about')
]
