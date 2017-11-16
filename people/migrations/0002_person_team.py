# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-06 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='team',
            field=models.CharField(choices=[('ED', 'Editorial'), ('EX', 'Exec'), ('EV', 'Events'), ('DS', 'Design'), ('WB', 'Web')], default='ED', max_length=2),
        ),
    ]