# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-14 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_called', models.BooleanField(default=False, verbose_name='Вже зателефоновано')),
            ],
        ),
    ]
