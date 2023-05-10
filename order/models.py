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
    user = models.CharField('Запросившый услугу', max_length=255, default='')
    additional = models.TextField('Описание задания', default='')
    staff = models.CharField('Работающий над проектом', max_length=255, default='')
    time_created = models.DateField('Дата создания', auto_now_add=True)
    cost = models.IntegerField('Минимальная цена')
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'