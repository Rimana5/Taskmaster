from django.urls import path
from . import views

urlpatterns = [
    # Пусть главная страница открывает home.html
    path('', views.home, name='home'),
    
    # Страница со стратегиями
    path('strategy/', views.strategy, name='strategy'),
    
    # Страница "Хронология" (опционально)
    path('history/', views.history, name='history'),
]
