# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-13 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_historial', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_paciente', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_procedimiento', models.CharField(max_length=60)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipoproducto', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipoproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.TipoProducto'),
        ),
        migrations.AddField(
            model_name='historial',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Paciente'),
        ),
        migrations.AddField(
            model_name='historial',
            name='producto',
            field=models.ManyToManyField(to='inventario.Producto'),
        ),
    ]