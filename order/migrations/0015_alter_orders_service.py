# Generated by Django 4.1.7 on 2023-05-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_rename_username_orders_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='service',
            field=models.IntegerField(default=0, verbose_name='ID УСЛУГИ'),
        ),
    ]
