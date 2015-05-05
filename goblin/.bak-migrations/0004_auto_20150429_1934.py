# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goblin', '0003_auto_20150429_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlink',
            name='project',
            field=models.ForeignKey(related_name='+', blank=True, to='goblin.Project', null=True),
            #preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectlink',
            name='release',
            field=models.ForeignKey(related_name='+', blank=True, to='goblin.Release', null=True),
            #preserve_default=True,
        ),
    ]
