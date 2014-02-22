from django import forms
from captcha.fields import ReCaptchaField

class CaptchaForm(forms.Form):
    captcha = ReCaptchaField()

class ContactForm(forms.Form):
    from_email = forms.EmailField()
    subject = forms.CharField(max_length=30)
    message = forms.CharField(max_length=400)
