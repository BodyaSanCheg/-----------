from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Асинхронность джанго
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

def register(request):
    """Регистрирует нового пользователя"""
    if request.method != 'POST':
        # Выводит пустую форму регистрации
        form = UserCreationForm
    else:
        # Обработка заполненной формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs:index')

    # Вывести пустую или недействительную форму
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def validate_username(request):
    """Проверка доступности логина"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    print(response)
    return JsonResponse(response)