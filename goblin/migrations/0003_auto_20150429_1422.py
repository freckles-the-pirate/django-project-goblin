# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goblin', '0002_projectlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlink',
            name='type',
            field=models.CharField(default=datetime.datetime(2015, 4, 29, 21, 22, 3, 951741, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectlink',
            name='url',
            field=models.URLField(default='about:blank'),
            preserve_default=False,
        ),
    ]
