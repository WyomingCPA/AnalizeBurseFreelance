from django.conf.urls import patterns, url, include
#from GPSApp.models import GPSCoordinates

import views


urlpatterns = patterns('',    
    url(r'^$', views.read_advert, name='read_advert'),
    url(r'^action_ads/$', views.action_advert, name='action_advert'),
) 