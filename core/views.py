from django.http import HttpResponse
from django.shortcuts import render

import httplib2
import os

from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from apiclient import discovery

import datetime
from dateutil import parser

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
	scopes = ['https://www.googleapis.com/auth/calendar.readonly']

	credentials = ServiceAccountCredentials.from_json_keyfile_name(
		os.path.join(os.path.dirname(__file__), '..', 'google_secret_key.json'), scopes)

	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)

	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	queryResult = service.events().list(
		calendarId='o5ne9e7vs8ggvdsr3lfd3ikv10@group.calendar.google.com',
		timeMin=now).execute()

	events = []
	curSide = "left"
	for event in queryResult.get('items', []):
		eventData = dict()


		# if event['start'].get('date') != None:
		# 	d = datetime.datetime.strptime(event['start'].get('date'), "%Y-%m-%d")
		# 	eventDate = d.strftime("%A %B %w, %Y")
		# else:
		# 	d = datetime.datetime.strptime(event['start'].get('dateTime'), "%Y-%m-%dTT%H:%M:%S%Z")
		# 	eventDate = d.strftime("%A %B %w, %Y")
		# print(type(event['start'].get('date')))
		# eventData['date'] = event['start'].get('dateTime', event['start'].get('date'))
		date = parser.parse(event['start'].get('dateTime', event['start'].get('date')))
		eventData['date'] = date.strftime("%A %B %W, %Y")
		# if

		eventData['title'] = event['summary']
		eventData['description'] = event['description']
		if 'location' in event:
			eventData['location'] = event['location']
		else:
			eventData['location'] = ""

		eventData['side'] = curSide
		if curSide == "left":
			curSide = "right"
		else:
			curSide = "left"

		events.append(eventData)

	context = {
		'events': events,
	}
	return render(request, 'events.html', context)

def maintenance(request):
	context = {}
	return render(request, 'construction.html', context)

def roster(request):
	context = {}
	return render(request, 'roster.html', context)

def competition(request):
	context = {} 
	return render(request, 'competition.html', context)