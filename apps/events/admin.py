from django.contrib import admin

from .models import Events


admin.site.register(Events)


class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
