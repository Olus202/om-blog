# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header',
            field=models.CharField(default='', max_length=200),
        ),
    ]
