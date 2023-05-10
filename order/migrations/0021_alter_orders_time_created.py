# Generated by Django 4.1.7 on 2023-05-10 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_alter_orders_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='time_created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]