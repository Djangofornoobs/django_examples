# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tablas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='jugado',
            field=models.CharField(default=b'S', max_length=1, choices=[(b'S', b'Si'), (b'N', b'No')]),
        ),
        migrations.AlterField(
            model_name='partido',
            name='goles_local',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='partido',
            name='goles_visitante',
            field=models.IntegerField(default=0),
        ),
    ]
