from django import forms

from .models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        field = ('name', 'lastname', 'email', 'position')
