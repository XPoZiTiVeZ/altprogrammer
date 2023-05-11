from django.db import models
from datetime import datetime

class Services(models.Model):
    title = models.CharField('Название', max_length=255, default='')
    lang = models.CharField('Язык программирования', max_length=255, default='')
    desc = models.CharField('Описание в услугах', max_length=255, default='')
    fulldesc = models.TextField('Описание в окне', blank=True)
    mincost = models.IntegerField('Минимальная цена')

    def __str__(self):
        return str(self.title + ' ' + self.lang + ' ' + str(self.mincost) + ' руб')
    
    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

class Orders(models.Model):
    service = models.IntegerField('ID УСЛУГИ', default=0)
    title = models.CharField('Название', max_length=255, default='')
    staff = models.CharField('Работающий над проектом', max_length=255, default='')
    user = models.CharField('Запросившый услугу', max_length=255, default='')
    additional = models.TextField('Описание задания', default='')
    time_created = models.DateField('Дата создания', auto_now_add=True)
    cost = models.IntegerField('Минимальная цена')
    
    def __str__(self):
        return f"{self.id} {self.title} {self.staff} {self.user} {self.time_created}"

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

class Chats(models.Model):
    title = models.CharField('Описание чата', max_length=255, default='')
    staff = models.CharField('Участник 1', max_length=255, default='')
    user = models.CharField('Участник 2', max_length=255, default='')
    time_created = models.DateField('Дата создания', auto_now_add=True)
    last_message = models.DateTimeField('Последнее сообщение', default=datetime.now())

    def __str__(self):
        return f"{self.id} {self.title} {self.staff} {self.user} {self.time_created}"

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

    def __str__(self):
        return f"{self.chat} {self.sender} {self.receiver} {self.time}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'