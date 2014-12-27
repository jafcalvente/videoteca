# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0003_auto_20141224_1035'),
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
    ]
