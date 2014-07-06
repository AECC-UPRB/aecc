from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'student_number', 'gender')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name',
                  'last_name', 'student_number', 'gender',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'student_number', 'gender',
                  'email')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.student_number = self.cleaned_data['student_number']
        user.gender = self.cleaned_data['gender']
        user.email = self.cleaned_data['email']
        user.save()


class SettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'email',
                  'courses', 'programming_languages', 'facebook', 'twitter',
                  'github', 'linkedin')

    def save_form(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.email = self.cleaned_data['email']
        user.courses = self.cleaned_data['courses']
        user.programming_languages = self.cleaned_data['programming_languages']
        user.facebook = self.cleaned_data['facebook']
        user.twitter = self.cleaned_data['twitter']
        user.github = self.cleaned_data['github']
        user.linkedin = self.cleaned_data['linkedin']
        user.save()
