# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the job title', max_length=300, verbose_name='title')),
                ('location', models.TextField(null=True)),
                ('offered_salary', models.TextField(null=True)),
                ('job_description', models.TextField(null=True)),
                ('no_of_vacancy', models.IntegerField(null=True)),
                ('job_specification', models.TextField(null=True)),
                ('educational_qualification', models.TextField(null=True)),
                ('url', models.URLField(blank=True, default=b'', max_length=500)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
