# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(default=b'---', max_length=3)),
                ('escudo', models.ImageField(upload_to=b'logos')),
                ('puntos', models.IntegerField(default=0)),
                ('goles_favor', models.IntegerField(default=0)),
                ('goles_contra', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goles_local', models.IntegerField()),
                ('goles_visitante', models.IntegerField()),
                ('equipo_local', models.ForeignKey(related_name='local', to='Tablas.Equipo')),
                ('equipo_visitante', models.ForeignKey(related_name='visitante', to='Tablas.Equipo')),
                ('jornada', models.ForeignKey(to='Tablas.Jornada')),
            ],
        ),
    ]
