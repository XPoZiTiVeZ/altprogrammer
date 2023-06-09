# Generated by Django 4.1.7 on 2023-05-10 20:34

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_alter_chatmessages_time_alter_chats_last_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessages',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 23, 34, 30, 622275), verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='chats',
            name='last_message',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 23, 34, 30, 621277), verbose_name='Последнее сообщение'),
        ),
        migrations.AlterField(
            model_name='chats',
            name='time_created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
