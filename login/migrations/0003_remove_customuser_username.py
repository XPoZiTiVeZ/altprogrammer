# Generated by Django 4.1.7 on 2023-04-05 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]