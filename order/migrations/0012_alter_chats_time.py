# Generated by Django 4.2 on 2023-05-04 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_chats_sendertype_alter_chats_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 19, 26, 39, 705183), verbose_name='Время'),
        ),
    ]
