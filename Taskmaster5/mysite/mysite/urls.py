from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls), #строка дообавления админа
    path('', include('polls.urls')),  
]
