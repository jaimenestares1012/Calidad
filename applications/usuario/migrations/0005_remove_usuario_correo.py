# Generated by Django 3.2.8 on 2021-11-12 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_usuario_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
    ]
