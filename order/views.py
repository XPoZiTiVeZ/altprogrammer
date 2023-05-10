from django.shortcuts import render, redirect
from .models import Services, Orders
from login.models import Chats
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

def services(request):
    services = Services.objects.all()
    return render(request, 'order/services.html', {'services':services})

@login_required
def neworder(request, id=None):
    service = Services.objects.get(id = id)
    if request.method == 'POST':
        additional = request.POST.get('additional')
        order = Orders(service = id, title = service.title + ' ' + service.lang, user = request.user.email, additional = additional, staff = "Lukashev", cost = 0)
        order.save()
        chat = Chats.objects.create(id = order.id, title = order.title, staff = order.staff, user = request.user.email)
        chat.save()
        return redirect('profile-orders')
    else:
        form = OrderForm()
        return render(request, 'order/addorder.html', {'service':service, 'form':form})