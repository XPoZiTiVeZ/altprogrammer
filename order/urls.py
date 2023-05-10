from django.urls import path
from . import views


urlpatterns = [
    path('services/', views.services, name='services'),
    path('services/neworder/<id>', views.neworder, name='neworder')
]