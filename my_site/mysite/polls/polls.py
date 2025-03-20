from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soldier/<int:pk>/', views.soldier_detail, name='soldier_detail'),
    path('barrack/<int:pk>/', views.barrack_detail, name='barrack_detail'),
]
