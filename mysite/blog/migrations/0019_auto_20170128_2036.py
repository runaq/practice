# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170128_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='static/img/', verbose_name='Ссылка картинки'),
        ),
    ]