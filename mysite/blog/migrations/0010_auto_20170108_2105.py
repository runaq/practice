# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170108_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='blog/images/', verbose_name='Ссылка картинки'),
        ),
    ]