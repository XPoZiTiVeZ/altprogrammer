from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('profile/<content>', views.profile, name='profile'),
    path('logout', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
]