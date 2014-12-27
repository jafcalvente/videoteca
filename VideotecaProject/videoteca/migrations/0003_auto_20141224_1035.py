# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0002_auto_20141224_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='plot',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
