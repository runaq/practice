# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_color', models.CharField(unique=True, max_length=20, verbose_name='Название')),
                ('color_number', models.CharField(max_length=6, verbose_name='RGB номер')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('author', models.CharField(max_length=200, verbose_name='Автор комментария')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата комментария')),
                ('approved_comment', models.BooleanField(default=False, verbose_name='Утвержден')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Название фрукта')),
                ('text', models.TextField(verbose_name='Описание')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(help_text='150x150px', upload_to='../media/', blank=True, verbose_name='Ссылка картинки')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('color', models.ForeignKey(to='blog.Color', to_field='name_color', verbose_name='Цвет')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post', verbose_name='Выберите цвет', related_name='comments'),
        ),
    ]
