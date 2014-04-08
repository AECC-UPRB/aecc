from django.shortcuts import render, redirect

from .forms import SignupForm


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/events/')
    data = {
        'form': form
    }
    return render(request, 'users/signup.html', data)
