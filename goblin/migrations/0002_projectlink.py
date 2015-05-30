# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goblin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.ForeignKey(related_name='urls', to='goblin.Project')),
                ('release', models.ForeignKey(related_name='urls', to='goblin.Release')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
