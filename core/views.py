from django.http import HttpResponse
from django.shortcuts import render

import datetime

from core.models import Event


def index(request):
    context = {}
    return render(request, 'sections/index.html', context)


def events(request):
    query = Event.objects.order_by('date').all().reverse()

    current_date = datetime.date.today()
    nearest_event = 0
    nearest_days = (query[0].date - current_date).days

    events = []
    for idx, elem in enumerate(query):
        date_delta = (elem.date - current_date).days
        if (date_delta > 0) and (nearest_days < 0 or (nearest_days > 0 and date_delta < nearest_days)):
            nearest_event = idx
            nearest_days = date_delta

        event = dict()
        event['id'] = idx
        event['title'] = elem.title
        event['image'] = elem.image.url[7:]

        event['location'] = elem.location
        event['full_date'] = elem.date.strftime("%A %B %d, %Y")
        event['short_date'] = elem.date.strftime("%m.%d.%y")
        if elem.start_time and elem.end_time:
            event['time'] = (elem.start_time.strftime("%I:%M%p").lstrip("0") + " - " +
                             elem.end_time.strftime("%I:%M%p").lstrip("0"))
        event['description'] = elem.description
        event['facebook'] = elem.facebook

        events.append(event)

    if nearest_days < 0:
        nearest_event = events[-1]['id']

    context = {
        'events': events,
        'nearest_event': nearest_event,
    }
    return render(request, 'sections/events.html', context)


def designpanel(request):
    return render(request, 'sections/designpanel.html', {})


def joinus(request):
    context = {}
    return render(request, 'sections/joinus.html', context)


def rawexpo(request):
    context = {}
    return render(request, 'sections/rawexpo.html', context)


def teams(request):
    context = {}
    return render(request, 'sections/teams.html', context)

def about(request):
    context = {}
    return render(request, 'sections/about.html', context)
