# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ad_date', models.DateField()),
                ('content', models.CharField(max_length=1000)),
                ('im_content', models.CharField(max_length=1000)),
                ('tags', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vk_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.IntegerField(choices=[('man', 0), ('woman', 1)])),
                ('ad_favor', models.ManyToManyField(to='easy.advert')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
