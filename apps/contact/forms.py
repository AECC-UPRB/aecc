from django import forms
from django.core.mail import send_mail

from captcha.fields import ReCaptchaField


class CaptchaForm(forms.Form):
    captcha = ReCaptchaField()


class ContactForm(forms.Form):
    from_email = forms.EmailField()
    subject = forms.CharField(max_length=30)
    message = forms.CharField(
        widget=forms.TextArea(),
        max_length=400)

    def send(self):
        from_email = self.cleaned_data['from_email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        recipients = ['example@example.com']
        send_mail(subject, message, from_email, recipients)
