# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0002_advert_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='ad_date',
            new_name='date',
        ),
    ]
