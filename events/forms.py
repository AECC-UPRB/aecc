from django import forms

from .models import Events


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('tittle', 'event_description', 'month', 'event_date', 'location', 'promo_picture')
