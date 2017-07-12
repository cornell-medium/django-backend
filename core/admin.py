from django.contrib import admin
from .models import Event, Image

admin.site.site_header = 'Medium Web Platform'


def make_visible(modeladmin, request, queryset):
    queryset.update(display='True')
make_visible.short_description = "Mark selected images as visible"


def make_invisible(modeladmin, request, queryset):
    queryset.update(display='False')
make_invisible.short_description = "Mark selected images as invisible"


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date')

admin.site.register(Event, EventAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('display', 'created_at')
    actions = [make_visible, make_invisible]

admin.site.register(Image, ImageAdmin)
