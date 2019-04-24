from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.creators, name='creators'),
    url(r'^profile/$', views.creators_profile, name='creators_profile'),
    url(r'^profile/splash/$', views.creators_profile_splash, name='creators_profile_splash'),
    url(r'^profile/edit/$', views.creators_edit_profile, name='creators_edit_profile'),
    url(r'^profile/new/$', views.creators_new_profile, name='creators_new_profile'),
    url(r'^project/$', views.creators_project, name='creators_project'),
    url(r'^project/new/$', views.creators_new_project, name='creators_new_project'),
    url(r'^project/preview/$', views.creators_preview_project, name='creators_preview_project'),
    url(r'^signin/$', views.creators_signin, name='creators_signin')
]