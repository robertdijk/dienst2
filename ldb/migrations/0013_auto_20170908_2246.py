# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-08 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldb', '0012_auto_20170106_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='emergency_name',
            field=models.CharField(blank=True, max_length=48, verbose_name='emergency name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_parents',
            field=models.CharField(blank=True, max_length=16, verbose_name='emergency phone'),
        ),
        migrations.RenameField(
            model_name='student',
            old_name='phone_parents',
            new_name='emergency_phone',
        ),
    ]
