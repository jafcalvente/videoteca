# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0004_auto_20141224_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.CharField(max_length=25, null=True, verbose_name=b'interpretes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=25, null=True, verbose_name=b'director'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=25, null=True, verbose_name=b'genero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.CharField(max_length=25, null=True, verbose_name=b'duracion'),
            preserve_default=True,
        ),
    ]
