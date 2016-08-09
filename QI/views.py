from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from models import Person
from models import Place
from models import Organization

def about(request):
	return render(request, 'about.html')

def texts(request):
	return render(request, 'texts.html')

def cornp1(request):
	return render(request, 'cornp1.html')

def places(request):
	return render(request, 'places.html')

def organizations(request):
	return render(request, 'organizations.html')



def profiles(request):
	person_list = Person.objects.order_by('last_name')
	place_list = Place.objects.order_by('name')
	org_list = Organization.objects.order_by('organization_name')
	return render(request, 'profiles.html', {'persons': person_list, 'places': place_list, 'orgs': org_list})

def storymap(request):
	return render(request, 'storymap.html')




def handler404(request):
	response = render_to_response('detail.html', {}, context_instance = RequestContext(request))
	response.status_code = 404
	return response




def handler500(request):
    response = render_to_response('detail.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

class Home(TemplateView):
	template_name = 'index.html'


