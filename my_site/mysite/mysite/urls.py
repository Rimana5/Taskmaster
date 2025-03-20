# mysite/urls.py

from django.contrib import admin
from django.urls import path, include  # Не забудьте импортировать include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),  # Подключаем маршруты из приложения polls
]
