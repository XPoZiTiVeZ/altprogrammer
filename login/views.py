from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.core.serializers import serialize
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .backends import CustomBackend
from order.models import Services, Orders, Chats, ChatMessages
from .forms import ChangeNameForm, SendMessage
from order.forms import OrderForm
from datetime import datetime
import base64

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            context = {'has_error': False, 'data': request.POST}
            email = request.POST.get('email')
            name =  request.POST.get('name')
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
            user.name = name
            user.save()
            return redirect('login')
    else:
        messages.warning(request, 'Вы уже имеете аккаунт')
        return redirect('home')
        
    return render(request, 'login/register.html')

def login_user(request):
    if not request.user.is_authenticated:
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
    else:
        messages.warning(request, 'Вы уже вошли аккаунт')
        return redirect('home')

@login_required
def profile(request):
    if request.user.is_worker:
        print(base64.urlsafe_b64encode(request.user.email.encode("utf-8")).decode('utf-8'))
        return render(request, 'login/info.html', {'code':base64.urlsafe_b64encode(request.user.email.encode("utf-8")).decode('utf-8')})
    return render(request, 'login/info.html')

@login_required
def profile_orders(request):
    orders = Orders.objects.filter(user = request.user.email)
    return render(request, 'login/orders.html', {'orders':orders})

@login_required
def profile_changename(request):
    if request.method == 'POST':
        new_name = request.POST.get('name')
        user = request.user
        user.name = new_name
        user.save()
        messages.success(request, 'Имя успешно изменено')
        return redirect('profile')
    else:
        form = ChangeNameForm()
        return render(request, 'login/changename.html', {'form':form})

@login_required
def profile_chats(request, id=None):
    orders = Orders.objects.filter(user = request.user.email)
    if len(orders) != 0:
        form = SendMessage()
        if id != None:
            if request.method == 'POST':
                chat = Chats.objects.get(id = id)
                chat.last_message = datetime.now()
                chat.save()
                chatmessage = ChatMessages.objects.create(chat = chat.id, message = request.POST.get('message'), sender = request.user.email, sendertype = 'staff' if request.user.is_worker else 'user', receiver = request.user.email if Orders.objects.get(id = id).user == request.user.email else Orders.objects.get(id = id).staff)
                chatmessage.save()
                return redirect('profile-chats', id = id)
            chats = Chats.objects.filter(user = request.user.email).order_by('-last_message')
            chatmessages = ChatMessages.objects.filter(chat = id)
            return render(request, 'login/chats.html', {'form':form, 'chats':chats, 'chatmessages':chatmessages, 'this_chat':Chats.objects.get(id = id)})
        else:
            chats = Chats.objects.filter(user = request.user.email).order_by('-last_message')
            return redirect('profile-chats', id = chats[0].id)
    else:
        return render(request, 'login/chats.html', {'noorders':True})
    


@login_required
def profile_cashin(request):
    return render(request, 'login/cashin.html')