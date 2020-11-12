from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
 
urlpatterns = [
    path('', views.home, name='home'),
    url('^index/(?P<trig>\d+)/$', views.index, name='index'),
    url(r'^notableCaptives/(?P<captiveid>\d+)/$', views.notableCaptives, name='notableCaptives'),
    url(r'^incomingCall/$', views.incomingCall, name='incomingCall'),
 ]