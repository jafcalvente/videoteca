# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0006_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='original_title',
            field=models.CharField(max_length=25, null=True, verbose_name=b't&iacute;tulo original'),
            preserve_default=True,
        ),
    ]
