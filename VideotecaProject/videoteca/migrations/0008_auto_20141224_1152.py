# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0007_movie_original_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.TextField(null=True, verbose_name=b'interpretes'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='original_title',
            field=models.CharField(default='N/A', max_length=25, verbose_name=b't\xc3\xadtulo original'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.TextField(null=True, verbose_name=b'sin\xc3\xb3psis'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.CharField(max_length=25, null=True, verbose_name=b'duraci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=25, verbose_name=b't\xc3\xadtulo'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True, verbose_name=b'a\xc3\xb1o'),
        ),
    ]
