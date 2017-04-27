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

import views

maintenance_mode = False

if maintenance_mode:
    urlpatterns = [
        url(r'^$', views.maintenance, name='maintenance'),
        url(r'^admin/', admin.site.urls),
    ]
else:
    urlpatterns = [
    	url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^apply/$', views.apply, name='apply'),
        url(r'^events/$', views.events, name='events'),
        url(r'^rawexpo/$', views.rawexpo, name='rawexpo'),
        url(r'^publication/$', views.publication, name='publication'),
        # url(r'^roster/$', views.roster, name='roster'),
        # url(r'^competition/$', views.competition, name='competition'),
        url(r'^admin/', admin.site.urls),
        # url(r'^pub/', include('articles.urls')),  # links to urlCONF in articles
    ]
