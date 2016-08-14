# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FreelanceAds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreelanceAdsHide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_check', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FreelanceAdsOverdue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_check', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='advertisingpost',
            name='ads_item',
        ),
        migrations.RemoveField(
            model_name='advertisingpost',
            name='user',
        ),
        migrations.AlterField(
            model_name='freelanceads',
            name='time_parsing',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='AdvertisingPost',
        ),
        migrations.AddField(
            model_name='freelanceadsoverdue',
            name='ads_item',
            field=models.ForeignKey(to='FreelanceAds.FreelanceAds'),
        ),
        migrations.AddField(
            model_name='freelanceadsoverdue',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='freelanceadshide',
            name='ads_item',
            field=models.ForeignKey(to='FreelanceAds.FreelanceAds'),
        ),
        migrations.AddField(
            model_name='freelanceadshide',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
