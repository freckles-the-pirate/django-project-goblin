# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import goblin.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=3, choices=[(b'+', b'Add'), (b'-', b'Remove'), (b'*', b'Fix'), (b'>', b'Other')])),
                ('what', models.TextField()),
            ],
            options={
                'verbose_name': 'Change',
                'verbose_name_plural': 'Changes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('slug', models.SlugField(help_text='Short name for the project', max_length=400)),
                ('description', models.TextField()),
                ('logo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('README', models.TextField(help_text='reStructuedText supported', null=True, blank=True)),
                ('homepage', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublishStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=100)),
                ('meaning', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', goblin.models.VersionField(max_length=30)),
                ('brief', models.TextField(help_text='What features are part of this release? Note that changes can be added with the <b>Changes</b> field.')),
                ('download', models.URLField(null=True, blank=True)),
                ('release_logo', models.ImageField(help_text="Leaving blank will use the project's logo.", null=True, upload_to=b'', blank=True)),
                ('release_date', models.DateField(help_text='When was this version released?', auto_now=True)),
                ('project', models.ForeignKey(to='goblin.Project')),
                ('status', models.ForeignKey(to='goblin.PublishStatus')),
            ],
            options={
                'verbose_name': 'Release',
                'verbose_name_plural': 'Releases',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(to='goblin.PublishStatus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='change',
            name='release',
            field=models.ForeignKey(to='goblin.Release'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='change',
            name='status',
            field=models.ForeignKey(to='goblin.PublishStatus'),
            preserve_default=True,
        ),
    ]
