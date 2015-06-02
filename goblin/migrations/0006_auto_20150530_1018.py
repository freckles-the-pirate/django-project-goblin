# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goblin', '0005_auto_20150430_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change',
            name='release',
            field=models.ForeignKey(related_name='+', to='goblin.Release'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectlink',
            name='project',
            field=models.ForeignKey(related_name='+', blank=True, to='goblin.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectlink',
            name='release',
            field=models.ForeignKey(related_name='+', blank=True, to='goblin.Release', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='release',
            name='project',
            field=models.ForeignKey(related_name='+', to='goblin.Project'),
            preserve_default=True,
        ),
    ]
