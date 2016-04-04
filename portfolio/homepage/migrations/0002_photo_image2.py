# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image2',
            field=models.ImageField(null=True, upload_to=b'static/images/', blank=True),
        ),
    ]
