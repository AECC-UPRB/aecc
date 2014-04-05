from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SignupForm


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/events/')
    data = {
        'form': form
    }
    return render(request, 'signup.html', data)
