# Generated by Django 3.2.8 on 2021-11-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0004_auto_20211118_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=20, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='actividades',
            name='fecha_reserva',
            field=models.DateField(max_length=200, verbose_name='fecha reserva'),
        ),
    ]
