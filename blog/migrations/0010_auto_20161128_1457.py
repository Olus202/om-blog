# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20161117_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='photos/posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.date(2016, 11, 28)),
        ),
    ]
