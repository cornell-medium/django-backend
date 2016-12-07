from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	context = {}
	return render(request, 'index.html', context)

def about(request):
	context = {}
	return render(request, 'about.html', context)

def events(request):
	context = {}
	return render(request, 'events.html', context)

def maintenance(request):
	context = {}
	return render(request, 'construction.html', context)

def roster(request):
	context = {}
	return render(request, 'roster.html', context)