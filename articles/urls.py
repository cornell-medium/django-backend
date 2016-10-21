from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<slug>[a-zA-Z_]+)/$', views.ArticleDetailView.as_view(), name='article-detail'),
    url(r'^page_(?P<page>[1-9]+)/$', views.ArticleListView.as_view(), name='article-list'),
    url(r'^$', views.ArticleListView.as_view(), name='article-list'),
]
