from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response

def about(request):
	return render(request, 'about.html')

def trans(request):
	return render(request, 'trans.html')


class Home(TemplateView):
	template_name = 'index.html'
