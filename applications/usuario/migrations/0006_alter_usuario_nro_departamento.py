# Generated by Django 3.2.8 on 2021-11-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_remove_usuario_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nro_departamento',
            field=models.IntegerField(unique=True, verbose_name='N° departamento'),
        ),
    ]
