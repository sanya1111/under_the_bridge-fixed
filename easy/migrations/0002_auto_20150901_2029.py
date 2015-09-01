# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='ad_rent',
        ),
        migrations.AddField(
            model_name='human',
            name='ad_rent',
            field=models.ManyToManyField(related_name='rent', to='easy.Advert'),
        ),
    ]
