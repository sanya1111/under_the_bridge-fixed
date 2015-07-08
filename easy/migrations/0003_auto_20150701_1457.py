# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0002_auto_20150701_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='ad_owner',
            field=models.ManyToManyField(to='easy.advert', related_name='ad_owner'),
        ),
        migrations.AlterField(
            model_name='human',
            name='ad_favor',
            field=models.ManyToManyField(to='easy.advert', related_name='ad_favor'),
        ),
    ]
