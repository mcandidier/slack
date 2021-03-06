# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 15:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_companymember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='companymember',
            unique_together=set([('company', 'member')]),
        ),
    ]
