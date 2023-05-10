# Generated by Django 4.1.7 on 2023-05-09 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_chats_last_message_alter_messages_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chats',
            old_name='member2',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='chats',
            old_name='member1',
            new_name='worker',
        ),
        migrations.AlterField(
            model_name='chats',
            name='last_message',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 21, 11, 2, 810307), verbose_name='Последнее сообщение'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 21, 11, 2, 811305), verbose_name='Время'),
        ),
    ]