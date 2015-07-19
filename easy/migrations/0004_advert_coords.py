# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0003_auto_20150716_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='coords',
            field=models.CharField(max_length=300, default=0),
            preserve_default=False,
        ),
    ]
