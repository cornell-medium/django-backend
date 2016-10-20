from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^(?P<slug>[a-zA-Z_]+)/$', views.ArticleDetailView.as_view(), name='article-detail'),
    url(r'^$', views.ArticleListView.as_view(), name='article-list'),
]
