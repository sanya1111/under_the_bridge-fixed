# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='adress',
            field=models.CharField(max_length=300, default='kut'),
            preserve_default=False,
        ),
    ]
