<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
=======
from django.shortcuts import render, redirect
>>>>>>> e58e33420508ae641ecd4ea573d48289457b65ab

from .forms import SignupForm
from .models import User


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
<<<<<<< HEAD
        messages.success(
            request,
            "Your data has been stored. " +
            "Remeber to contact any directive member to pay your membership")
        return HttpResponseRedirect('/members/signup/')
=======
        return redirect('/events/')
>>>>>>> e58e33420508ae641ecd4ea573d48289457b65ab
    data = {
        'form': form
    }
    return render(request, 'users/signup.html', data)


def directive_view(request):
    data = {
        'people_information': User.objects.all()
    }
    return render(request, 'users/directive.html', data)
