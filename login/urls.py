from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/orders', views.profile_orders, name='profile-orders'),
    path('profile/chats/', views.profile_chats, name='profile-chats'),
    path('profile/chats/<id>', views.profile_chats, name='profile-chats'),
    path('profile/changename', views.profile_changename, name='profile-changename'),
    path('profile/deposit', views.profile_cashin, name='profile-cashin'),
    path('logout', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
]