from django.http import HttpResponse
from django.shortcuts import render

import httplib2
import os

from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from apiclient import discovery

import datetime
import pytz
from dateutil import parser

from core.models import Event

def index(request):
	context = {}
	return render(request, 'index.html', context)

def about(request):
	context = {}
	return render(request, 'about.html', context)

def apply(request):
	context = {}
	return render(request, 'noapply.html', context)

def events(request):
	query = Event.objects.order_by('date').all()

	events = []
	for idx, elem in enumerate(query):
		event = dict()
		event['id'] = idx
		event['title'] = elem.title
		event['image'] = elem.image.url[7:]

		event['location'] = elem.location
		event['full_date'] = elem.date.strftime("%A %B %d, %Y")
		event['short_date'] = elem.date.strftime("%m.%d.%y")
		event['time'] = (elem.start_time.strftime("%I:%M%p").lstrip("0") + "-" +
						elem.end_time.strftime("%I:%M%p").lstrip("0"))
		event['description'] = elem.description

		events.append(event)

	context = {
		'events': events,
	}
	return render(request, 'events.html', context)

def maintenance(request):
	context = {}
	return render(request, 'construction.html', context)

def rawexpo(request):
	context = {}
	return render(request, 'rawexpo.html', context)

def roster(request):
	context = {}
	return render(request, 'roster.html', context)

def competition(request):
	context = {} 
	return render(request, 'competition.html', context)