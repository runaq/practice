# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170108_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='../images/', verbose_name='Ссылка картинки'),
        ),
    ]