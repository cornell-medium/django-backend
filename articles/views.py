from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


# Create your views here.
class ArticleDetailView(DetailView):

    model = Article
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class ArticleListView(ListView):

    paginate_by = 5
    paginate_orphans = 3
    model = Article
    context_object_name = 'articles_list'
