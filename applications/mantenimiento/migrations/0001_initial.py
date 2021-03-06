# Generated by Django 3.2.8 on 2021-10-31 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trabajo_mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_trabajadores', models.IntegerField(verbose_name='N° trabajadores')),
                ('dia_mantenimiento', models.DateTimeField(verbose_name='Fecha')),
                ('hora_mantenimiento', models.IntegerField(choices=[('5', '05 am'), ('6', '06 am'), ('7', '07 am'), ('8', '08 am'), ('9', '09 am'), ('10', '10 am'), ('11', '11 am'), ('12', '12 pm'), ('13', '01 pm'), ('14', '02 pm'), ('15', '03 pm'), ('16', '04 pm'), ('17', '05 pm'), ('18', '06 pm'), ('19', '07 pm'), ('20', '08 pm'), ('21', '09 pm'), ('22', '10 pm'), ('23', '11 pm'), ('24', '12 am'), ('1', '01 am'), ('2', '02 am'), ('3', '03 am'), ('4', '04 am')], verbose_name='Hora')),
            ],
            options={
                'verbose_name': 'Mantenimiento',
                'verbose_name_plural': 'Trabajos de mantenimientos',
                'ordering': ['dia_mantenimiento'],
            },
        ),
        migrations.CreateModel(
            name='Externos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_externo', models.IntegerField(verbose_name='Dni externo')),
                ('nombre_externo', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido_externo', models.CharField(max_length=50, verbose_name='apellido')),
                ('trabajo_mantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.trabajo_mantenimiento')),
            ],
            options={
                'verbose_name': 'Externos',
                'verbose_name_plural': 'Trabajadores externos',
            },
        ),
    ]
