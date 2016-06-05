from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.core import management, serializers
from models import Person
from models import Place
from models import Org
from models import Relationship
from models import Page
from models import Manuscript

import os
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


#becky is adding this next few as a test to see if a given person/place/org page will work
def person_detail(request,id):
	try:
		person = Person.objects.get(id_tei = id)
		#birthplace = Place.objects.get(id_tei = person.birth_place)
		#deathplace = Place.objects.get(id_tei = person.death_place)
	except Person.DoesNotExist:
		raise Http404('this person does not exist')
	return render(request,'person_detail.html',{
	'person':person,
	#'birthplace':birthplace,'deathplace':deathplace
	})

def place_detail(request,id):
	try:
		place = Place.objects.get(id_tei = id)
	except Place.DoesNotExist:
		raise Http404('this place does not exist')
	return render(request,'place_detail.html',{
	'place':place,
	})

def org_detail(request,id):
	try:
		org = Org.objects.get(id_tei = id)
		#place = Place.objects.get(id_tei = org.place_id)
	except Org.DoesNotExist:
		raise Http404('this organization does not exist')
	return render(request,'org_detail.html',{
	'org':org,
	#'place':place
	})


def pageinfo(request,id):
	try:
		page = Page.objects.get(id_tei = id)
		manuscript = Manuscript.objects.get(title = page.Manuscript_id)
	except Page.DoesNotExist:
		raise Http404('this page does not exist')
	#need to go through manuscript pages and determine which is first and which is last !
	#mostly just which is last bc i think first is always 001
	try:
		IsNextPage = True #set this true by default; says there is a next page
		newid = int(id)
		newid = newid+1 #next page in manuscript
		#now we need to turn it back into a proper string
		newstring = str(newid)
		if len(newstring) == 2:
			newstring = "0" + newstring
		elif len(newstring) == 1:
			newstring = "00" + newstring
		nextpage = Page.objects.get(id_tei = newstring) #see if next page in manuscript exists
	except Page.DoesNotExist:
		IsNextPage = False
	try:
		IsPreviousPage = True #set this true by default
		newid1 = int(id)
		newid1 = newid1 - 1
		#now we must turn it into a proper string
		newstring1 = str(newid1)
		if len(newstring1) == 2:
			newstring1 = "0" + newstring1
		elif len(newstring1) == 1:
			newstring1 = "00" + newstring1
		prevpage = Page.objects.get(id_tei = newstring1) # see if previous page in manuscript exists
	except Page.DoesNotExist:
		IsPreviousPage = False
	return render(request,'page_detail.html', {
	'page':page,'manuscript':manuscript, 'IsNextPage':IsNextPage, 'IsPreviousPage':IsPreviousPage
	})

	#gotta include info as to whether or not it's the first or last pg in a manuscript!

def pagejsoninfo(request,id):
	try:
		items = serializers.serialize("json",[Manuscript.objects.get(id_tei=id)])
	except Manuscript.DoesNotExist:
		raise Http404('this manuscript does not exist')
	return HttpResponse(items, content_type='application/json')

def htmlinfo(request):
	orgs = Organization.objects.all()
	persons = Person.objects.all()
	places = Place.objects.all()
	return render(request, 'test.html', {
	'orgs':orgs,'persons':persons,'places':places
	})

def jsoninfo(request,id):
	# data = serializers.serialize("json",Person.objects.get(id_tei=id))
	try:
		items = serializers.serialize("json",[Person.objects.get(id_tei=id)])
		#ok so this above statement works but it is not what i want. i want a list of one person. help
		# maybe ill just put brackets?? around something?
	except Person.DoesNotExist:
		try:
			items = serializers.serialize("json",[Place.objects.get(id_tei=id)])
		except Place.DoesNotExist:
			try:
				items = serializers.serialize("json",[Org.objects.get(id_tei=id)])
			except Org.DoesNotExist:
				raise Http404('this item does not exist')
	return HttpResponse(items, content_type='application/json')

#this is the end of what becky did

def profiles(request):
	person_list = Person.objects.order_by('last_name')
	place_list = Place.objects.order_by('name')
	org_list = Org.objects.order_by('organization_name')
	return render(request, 'profiles.html', {'persons': person_list, 'places': place_list, 'orgs': org_list})

def storymap(request, xml_id):
	return render(request, 'story_maps/' + xml_id + '.html')

def storymap_dir(request):
	return render(request, 'storymap_dir.html')
def SMimport(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		the_file = request.FILES['datafile']
		request.FILES['datafile'].name
		fileName = request.FILES['datafile'].name
		#takes off the .xml because of the way generate.py works
		#also, this is a way to check to file type is correct
		#Really, it's a bad way
		trunc_fileName=""
		afterdot=False
		fileType=""
		for char in fileName:
			if afterdot:
				fileType=fileType+char
				continue
			if char <> '.':
				trunc_fileName=trunc_fileName+char
			else:
				afterdot=True
				continue
		if fileType <> "xml":
			print "Needs to be a .xml file"
			#it would be sick if a had an error message or page
			return render(request, '../templates/admin/SMimport/index.html',{'failed' : True})
		print fileType
		print trunc_fileName
		print fileName
		print '/static/xml/'+fileName
		#This is pretttty hacky and may have some problems
		#I am changing the working directory so that python writes it into the spot I want it to
		#Is there a better way to do this? Probably. Can probably do it where you open the file, but that wasn't working for me
		current_directory=os.getcwd()
		print current_directory, type(current_directory)
		os.chdir(current_directory+"/static/xml")
		print os.getcwd()
		with open(fileName,'w') as f:
			print "we did it"
			a=the_file.read()
			#print a
			f.write(a)
		os.chdir(current_directory)
		management.call_command('generate',trunc_fileName)
		return render(request, '../templates/admin/SMimport/index.html',{"success" : True})
	else:
		return render(request, '../templates/admin/SMimport/index.html')

def XMLimport(request):
# if this is a POST request we need to process the form data
	if request.method == 'POST':
		the_file = request.FILES['datafile']
		request.FILES['datafile'].name
		fileName = request.FILES['datafile'].name
		selected=request.POST['selected']

		#NOT SURE IF THIS WORKS THE SAME WAY, THINK IT NEEDS THE WHOLE PATH AS THE NAME?
		#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV


		#takes off the .xml because of the way generate.py works
		#also, this is a way to check to file type is correct
		#Really, it's a bad way
		trunc_fileName=""
		afterdot=False
		fileType=""
		for char in fileName:
			if afterdot:
				fileType=fileType+char
				continue
			if char <> '.':
				trunc_fileName=trunc_fileName+char
			else:
				afterdot=True
				continue
		if fileType <> "xml":
			print "Needs to be a .xml file"
			#it would be sick if a had an error message or page
			return render(request, '../templates/admin/XMLimport/index.html',{'failed' : True})
		print fileType
		print trunc_fileName
		print fileName
		print '/static/xml/'+fileName

		#This is pretttty hacky and may have some problems
		#I am changing the working directory so that python writes it into the spot I want it to
		#Is there a better way to do this? Probably. Can probably do it where you open the file, but that wasn't working for me
		current_directory=os.getcwd()
		print current_directory, type(current_directory)
		os.chdir(current_directory+"/static/AutoModels")
		filepath = os.getcwd()
		with open(fileName,'w') as f:
			a=the_file.read()
			f.write(a)
		if selected == 'page_break':
			with open(trunc_fileName+'.html','w') as f:
				a=the_file.read()
				f.write(a)
		os.chdir(current_directory)
		if selected == 'xml':
			management.call_command('XML_to_HTML',filepath+'/'+fileName)
		elif selected == 'page_break':
			management.call_command('admin_page_break_csv',filepath+'/'+fileName,filepath+'/'+trunc_fileName+".html")
		else:
			return render(request, '../templates/admin/XMLimport/index.html',{'failed' : True})
		return render(request, '../templates/admin/XMLimport/index.html',{"success" : True})
	else:
		return render(request, '../templates/admin/XMLimport/index.html')
class Home(TemplateView):
	template_name = 'index.html'
