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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('adress', models.CharField(max_length=300)),
                ('owner_type', models.BooleanField(choices=[('OWNER', False), ('RENTER', True)], default='OWNER')),
                ('coords_x', models.DecimalField(decimal_places=5, max_digits=30)),
                ('coords_y', models.DecimalField(decimal_places=5, max_digits=30)),
                ('content', models.CharField(max_length=1000)),
                ('im_content', models.CharField(max_length=1000)),
                ('tags', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('bum_coords', models.CharField(max_length=300)),
                ('ad_favor', models.ManyToManyField(to='easy.Advert')),
                ('ad_owner', models.ManyToManyField(to='easy.Advert', related_name='owner')),
                ('ad_rent', models.ForeignKey(to='easy.Advert', related_name='rent')),
            ],
        ),
    ]
