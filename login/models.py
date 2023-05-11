from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from datetime import datetime

class CustomUser(AbstractUser):
    username = None
    name = models.CharField('Обращение к пользователю', max_length=255, blank=True)
    email = models.EmailField(_('почта'), unique=True)
    is_email_verified = models.BooleanField(_('подтверждённый'), default=False)
    is_worker = models.BooleanField('Работник', default=False)
    vmoney = models.IntegerField('Деньги', default=0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username} профиль'