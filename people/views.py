from django.shortcuts import render_to_response
from people.models import People
# Create your views here.
def people_view(request):
	args = {}
	args['peopleInStorage'] = People.objects.all()
	return render_to_response('people.html', args)