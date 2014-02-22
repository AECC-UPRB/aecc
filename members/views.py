from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from members.forms import SignupForm


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your data has been stored. Remeber to contact any directive member to pay your membership")
        return HttpResponseRedirect('/signup/')
    data = {
        'form': form
    }
    return render(request, 'signup.html', data)
