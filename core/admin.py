from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import Event

admin.site.site_header = 'Medium Web Platform'

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date')

admin.site.register(Event, EventAdmin)

