# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_check', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FreelanceAds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('text', models.CharField(max_length=2000)),
                ('site', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('time_parsing', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='advertisingpost',
            name='ads_item',
            field=models.ForeignKey(to='FreelanceAds.FreelanceAds'),
        ),
        migrations.AddField(
            model_name='advertisingpost',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
