# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_photo_image2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='overlay',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='image2',
            new_name='thumbnail',
        ),
    ]
