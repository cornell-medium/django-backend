from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.creators, name='creators'),
    url(r'^new_project/$', views.creators_new, name='creators_new'),
    url(r'^signin/$', views.creators_signin, name='creators_signin')
]

    