# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-09 12:04
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_html',
            field=DjangoUeditor.models.UEditorField(blank=True, default='images/1.jpg', verbose_name='文章内容'),
        ),
    ]
