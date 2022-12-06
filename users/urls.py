"""Опеределение схемы URL для Users"""

from django.urls import path, include
from . import views
from django.contrib.auth import urls

app_name = 'users'

urlpatterns = [
    # Включить URL вторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации
    path('register/', views.register, name='register'),
    # Асинхронный запрос
    path('ajax/', views.validate_username, name='validate_username'),
]
