from django.shortcuts import render, redirect
from .models import Services, Orders, Chats
from login.models import CustomUser
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from random import choice
import base64

def workers(workers, user):
    updated_workers = []
    for worker in workers:
        if worker == 'lukashevda@inbox.ru':
            w = [worker] * 3
            updated_workers += w
        else:
            updated_workers.append(worker)
        # if worker != user:
    return updated_workers

def services(request):
    try:
        code = request.GET['code']
        services = Services.objects.all()
        return render(request, 'order/services.html', {'services':services, 'code':code})
    except:
        services = Services.objects.all()
        return render(request, 'order/services.html', {'services':services, 'code':False})

@login_required
def neworder(request, id=None, code=None):
    service = Services.objects.get(id = id)
    if request.method == 'POST':
        additional = request.POST.get('additional')
        try:
            code = request.GET['code']
            order = Orders(service = id, title = service.title + ' ' + service.lang, user = request.user.email, additional = additional, staff = base64.urlsafe_b64decode(code).decode('utf-8'), cost = 0)
        except:
            order = Orders(service = id, title = service.title + ' ' + service.lang, user = request.user.email, additional = additional, staff = choice(workers(list(map(lambda user: user.email ,CustomUser.objects.filter(is_worker = True))), request.user.email)), cost = 0)
        order.save()
        chat = Chats.objects.create(id = order.id, title = order.title, staff = order.staff, user = request.user.email)
        chat.save()
        return redirect('profile-orders')
    else:
        form = OrderForm()
        return render(request, 'order/addorder.html', {'service':service, 'form':form, 'code':code})