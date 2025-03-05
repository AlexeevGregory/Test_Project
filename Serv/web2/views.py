from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from random import randint

from django.http import JsonResponse
import logging

from django.views.decorators.csrf import csrf_exempt


def generate_code():
    return str(randint(1000, 9999))

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('generate_code')  # Убедитесь, что это правильный путь
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def generate_code_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    val = generate_code()
    context = {'val': val}
    return render(request, 'index.html', context)

from django.views.decorators.csrf import csrf_exempt

import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logger.info(f'User  {request.user.username} is logging out via page refresh.')
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)