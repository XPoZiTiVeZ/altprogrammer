from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .backends import CustomBackend

def register(request):
    if request.method == 'POST':
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
    
        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Пароли не совпадают')
            context['has_error'] = True

        if CustomUser.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Такая почта уже зарегистрирована')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'login/register.html', context)
        
        user = CustomUser.objects.create_user(email=email, password=password)
        user.save()
        return redirect('login')
        
    return render(request, 'login/register.html')

def login_user(request):
    if request.method == "POST":
        context = {'data': request.POST}
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomBackend.authenticate(request, username=email, password=password)

        if user and not user.is_email_verified and False:
            messages.add_message(request, messages.ERROR,
                                 'Почта не подтверждена, пожалуйста проверьте почту')
            return render(request, 'login/login.html', context)
        
        if user and not user.is_active:
            messages.add_message(request, messages.ERROR,
                                 'Аккаунт ещё не подтверждён администратором, если вы считаете, что это ошибка, напишите в тех. поддержку')
            return render(request, 'login/login.html', context)

        if not user:
            messages.add_message(request, messages.ERROR, 'Неправильная почта или пароль')
            return render(request, 'login/login.html', context)
    
        login(request, user)

        messages.add_message(request, messages.SUCCESS, f'Добро пожаловать, {user.last_name} {user.first_name}')
        return redirect('home')
    return render(request, 'login/login.html')

@login_required
def profile(request, content):
    if content == 'orders':
        oblast = 'orders'
        return render(request, 'login/profile.html', {'oblast':oblast})
    elif content == 'messages':
        oblast = 'messages'
        return render(request, 'login/profile.html', {'oblast':oblast})