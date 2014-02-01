from django import forms

from people.models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        field = ('name', 'lastname', 'email', 'position')
