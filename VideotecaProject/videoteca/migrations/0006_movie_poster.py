# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0005_auto_20141224_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=100, null=True, verbose_name=b'poster'),
            preserve_default=True,
        ),
    ]
