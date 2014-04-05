from django.shortcuts import render_to_response


def home_view(request):
    return render_to_response('static/home.html')


def about_view(request):
    return render_to_response('static/about.html')
