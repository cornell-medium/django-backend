"""mediumsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^creators/$', views.creators, name='creators'),
    url(r'^creators_new/$', views.creators_new, name='creators_new'),
    url(r'^creators_main/$', views.creators_main, name='creators_main'),
    url(r'^creators_signin/$', views.creators_signin, name='creators_signin'),
    url(r'^events/$', views.events, name='events'),
    url(r'^designpanel/$', views.designpanel, name='designpanel'),
    url(r'^joinus/$', views.joinus, name='joinus'),
    url(r'^login/$', views.login, name='login'),
    url(r'^raw/$', views.rawexpo, name='rawexpo'),
    url(r'^teams/$', views.teams, name='teams'),
]
