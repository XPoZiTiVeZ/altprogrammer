# Generated by Django 4.1.7 on 2023-04-16 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orders_options_orders_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='language',
            new_name='lang',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='cost',
            new_name='mincost',
        ),
    ]
