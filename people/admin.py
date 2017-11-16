from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from models import Person

admin.site.site_header = 'People Admin'


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

admin.site.register(Person, PersonAdmin)
