# Generated by Django 4.1.7 on 2023-05-10 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_rename_client_chats_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='order',
        ),
        migrations.AlterField(
            model_name='chats',
            name='last_message',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 22, 27, 59, 311636), verbose_name='Последнее сообщение'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 22, 27, 59, 313194), verbose_name='Время'),
        ),
    ]