from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title_slug": ("title",)}
    prepopulated_fields = {"month_slug": ("month",)}


admin.site.register(Event, EventAdmin)
