# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('ad_date', models.DateField()),
                ('content', models.CharField(max_length=1000)),
                ('im_content', models.CharField(max_length=1000)),
                ('tags', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('vk_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('ad_favor', models.ManyToManyField(to='easy.Advert')),
                ('ad_owner', models.ManyToManyField(to='easy.Advert', related_name='owner')),
            ],
        ),
    ]
