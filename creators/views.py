# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import models    

def index(request):
    render(request, 'sections/index.html', {})

def home(request):
    render(request, 'sections/home.html', {})

def projects(request):
    query = Project.objects.order_by('date').all().reverse()
    projects = []
    for p in query:
        project = {}

        project['name'] = p.name
        project['description'] = p.description 
        project['start_date'] = p.date.strftime("%A %B %d, %Y") 
        project['end_date'] = p.date.strftime("%A %B %d, %Y") 
        project['external_link'] = p.external_link


        ### Not sure exactly what data from contributor is wanted.

        # project['contributors'] = p.contributor 
        # project['images'] = p.images
        # project['tags'] = p.tags

        projects.append(project)

    context = 
    {
    'projects': projects
    }
    render(request, 'sections/projects.html', context)

def profile(request):
    render(request, 'sections/profile.html', context)

def account(request):
    render(request, 'sections/account.html', context)


