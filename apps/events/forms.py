from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'month',
                  'event_date', 'location', 'promo_picture')
