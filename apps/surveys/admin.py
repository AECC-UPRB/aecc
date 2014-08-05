from django.contrib import admin

from .models import Survey, Poll, Choice

admin.site.register(Survey)
admin.site.register(Poll)
admin.site.register(Choice)
