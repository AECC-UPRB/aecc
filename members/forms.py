from django import forms

from models import Member


class SignupForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'gender', 'email']
