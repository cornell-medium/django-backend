# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def creators(request):
    context = {}
    return render(request, 'sections/creators_index.html', context)


def creators_new(request):
    context = {}
    return render(request, 'sections/creators_newproject.html', context)


def creators_signin(request):
    context = {}
    return render(request, 'sections/creators_signin.html', context)