# Generated by Django 3.2.8 on 2022-01-11 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_alter_usuario_nro_departamento'),
        ('mantenimiento', '0005_trabajo_mantenimiento_nro_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo_mantenimiento',
            name='usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
            preserve_default=False,
        ),
    ]
