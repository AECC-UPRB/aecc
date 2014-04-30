from django import forms

from models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'student_number', 'gender',
                  'email']
