# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170108_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='blog/templates/blog/images/', verbose_name='Ссылка картинки'),
        ),
    ]