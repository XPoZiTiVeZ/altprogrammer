# Generated by Django 4.1.7 on 2023-05-10 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_chatmessages_delete_messages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessages',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 23, 29, 44, 273550), verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='chats',
            name='last_message',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 23, 29, 44, 272511), verbose_name='Последнее сообщение'),
        ),
    ]
