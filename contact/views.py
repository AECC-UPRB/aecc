from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import ContactForm


def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recipients = ['emma.luciano11@gmail.com']
            send_mail(subject, message, from_email, recipients)
            return HttpResponseRedirect('/home/')
    else:
        data = {
            'form': ContactForm()
        }
    return render(request, 'contact_us.html', data)
