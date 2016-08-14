# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User



#Модель объявления
class FreelanceAds(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=2000)
    site = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    time_parsing = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.title

#Скрыть объявления 
class FreelanceAdsHide(models.Model):
    user = models.ForeignKey(User)
    ads_item = models.ForeignKey(FreelanceAds)
    time_check = models.DateTimeField(auto_now = True)

#Просроченные объявления
class FreelanceAdsOverdue(models.Model):
    user = models.ForeignKey(User)
    ads_item = models.ForeignKey(FreelanceAds)
    time_check = models.DateTimeField(auto_now = True)


