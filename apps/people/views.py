from django.shortcuts import render_to_response

from .models import People


def people_view(request):
    data = {
        'people_information': People.objects.all()
    }
    return render_to_response('people.html', data)
