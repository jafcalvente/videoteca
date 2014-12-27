# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.TextField(null=True, verbose_name=b'sinopsis'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True, verbose_name=b'a&ntilde;o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=25, verbose_name=b't&iacute;tulo')
        ),
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.ForeignKey(verbose_name=b'formato', to='videoteca.MovieType'),
        ),
        migrations.AlterField(
            model_name='movietype',
            name='type',
            field=models.CharField(max_length=10, verbose_name=b'formato'),
        ),
    ]
