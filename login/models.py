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
    
class Chats(models.Model):
    title = models.CharField('Описание чата', max_length=255, default='')
    staff = models.CharField('Участник 1', max_length=255, default='')
    user = models.CharField('Участник 2', max_length=255, default='')
    time_created = models.DateField('Дата создания', auto_now_add=True)
    last_message = models.DateTimeField('Последнее сообщение', default=datetime.now())

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

class ChatMessages(models.Model):
    chat = models.IntegerField('Id чата', default=0)
    message = models.TextField('Сообщение', max_length=500, default='')
    sender = models.CharField('Отправитель', max_length=255, default='')
    sendertype = models.CharField('Тип отправителя', max_length=255, default='')
    receiver = models.CharField('Получатель', max_length=255, default='')
    time = models.DateTimeField('Время', default=datetime.now())

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'