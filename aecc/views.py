from django.shortcuts import render_to_response


def home_view(request):
    return render_to_response('home.html')


def about_view(request):
    return render_to_response('about.html')
