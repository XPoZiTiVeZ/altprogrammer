# Generated by Django 4.1.7 on 2023-05-09 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_chats_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chats',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='service_id',
            new_name='service',
        ),
    ]
