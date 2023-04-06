from django.shortcuts import render

def home(request):
    return render(request, 'page/home.html')

def services(request):
    return render(request, 'page/services.html')