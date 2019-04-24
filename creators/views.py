# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def creators(request):
    context = {}
    return render(request, 'sections/creators_index.html', context)


def creators_profile(request):
    context = {}
    return render(request, 'sections/creators_profile.html', context)


def creators_edit_profile(request):
    context = {}
    return render(request, 'sections/creators_editprofile.html', context)


def creators_profile_splash(request):
    context = {}
    return render(request, 'sections/creators_profilesplash.html', context)


def creators_new_profile(request):
    context = {}
    return render(request, 'sections/creators_newprofile.html', context)


def creators_project(request):
    context = {}
    return render(request, 'sections/creators_project.html', context)


def creators_new_project(request):
    context = {}
    return render(request, 'sections/creators_newproject.html', context)


def creators_preview_project(request):
    context = {}
    return render(request, 'sections/creators_preview.html', context)


def creators_signin(request):
    context = {}
    return render(request, 'sections/creators_signin.html', context)