# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0004_advert_coords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='coords',
        ),
        migrations.AddField(
            model_name='advert',
            name='coords_x',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advert',
            name='coords_y',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=30),
            preserve_default=False,
        ),
    ]
