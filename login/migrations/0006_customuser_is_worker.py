# Generated by Django 4.2 on 2023-05-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_worker',
            field=models.BooleanField(default=False, verbose_name='Работник'),
        ),
    ]