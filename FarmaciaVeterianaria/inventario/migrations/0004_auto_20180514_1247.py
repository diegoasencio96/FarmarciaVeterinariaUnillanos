# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-14 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20180513_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paciente.Paciente'),
        ),
        migrations.AlterField(
            model_name='procedimiento',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paciente.Paciente'),
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
    ]