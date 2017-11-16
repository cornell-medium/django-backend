from django.shortcuts import render
from models import Person


# Create your views here.
def people_view(request):
    return render(request, template_name='sections/people.html', context={'people': Person.objects.all()})
