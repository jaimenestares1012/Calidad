# Generated by Django 3.2.8 on 2021-10-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_usuario', models.IntegerField(verbose_name='Dni')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('nro_departamento', models.IntegerField(verbose_name='N° departamento')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo')),
                ('celular', models.IntegerField(verbose_name='Celular')),
            ],
        ),
    ]
