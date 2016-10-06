from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.core import management, serializers
from reportlab.pdfgen import canvas
from io import BytesIO
from models import Person
from models import Place
from models import Org
from models import Relationship
from models import Page
from models import Manuscript
from HTMLParser import HTMLParser
import zipfile as z
import StringIO as cs
from tempfile import *

import os
def about(request):
	return render(request, 'about.html')

def mapgallery(request):
	return render(request, 'mapgallery.html')

def historicalbackground (request):
	return render(request, 'historicalbackground.html')

def manuscripts(request):
	textlist = Manuscript.objects.order_by('title')
	pagelist = Page.objects.order_by('Manuscript_id')
	return render(request, 'manuscripts.html', {'textlist':textlist,'pagelist':pagelist})

def profiles(request):
	person_list = Person.objects.order_by('last_name')
	place_list = Place.objects.order_by('name')
	org_list = Org.objects.order_by('organization_name')
	return render(request, 'profiles.html', {'persons': person_list, 'places': place_list, 'orgs': org_list})

def cornp1(request):
	return render(request, 'cornp1.html')

def places(request):
	return render(request, 'places.html')

def organizations(request):
	return render(request, 'organizations.html')

def testsearch(request):
	return render(request, 'testsearch.html')

def testsearch2(request):
	return render(request, 'testsearch2.html')

def search(request):
	return render(request, 'search/search.html')

def overviewmap_traveler(request):
	return render(request, 'overviewmap_traveler.html')

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

def overviewmap_date(request):
	return render(request, 'overviewmap_date.html')

def overviewmap_residence(request):
	return render(request, 'overviewmap_residence.html')

def overviewmap_popularlocations(request):
	return render(request, 'overviewmap_popularlocations.html')

def usingthesite(request):
	return render(request, 'usingthissite.html')

def bibliography(request):
	return render(request, 'bibliography.html')

def credits(request):
	return render(request, 'credits.html')

def mapgallery(request):
	return render(request, 'mapgallery.html')
	
def outputPagePDF(request,id):
	PageToOutput = Page.objects.get(id_tei = id) #get the Page that you want to output!
	FullText = PageToOutput.fulltext #get the text that you want to put in the PDF
    # Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
	buffer = BytesIO()
    # Create the PDF object, using the BytesIO object as its "file."
	p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
	p.drawString(100, 100, "Hello world.")
    # Close the PDF object cleanly.
	p.showPage()
	p.save()
    # Get the value of the BytesIO buffer and write it to the response.
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response

class MLStripper(HTMLParser): #This Class is used in the following view, outputPagePT, to get txt file of a page
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def outputPagePT(request,id):
	PageToOutput = Page.objects.get(id_tei = id) #get the Page that you want to output!
	FullText = PageToOutput.fulltext #get the text that you want to put in the PDF
	s = MLStripper()
	s.feed(FullText)
	newtext = s.get_data()
	response = HttpResponse(newtext, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename="%s.txt"' % PageToOutput.id_tei
	return response

def outputManuPT(request,id):
	ManuToOutput = Manuscript.objects.get(id_tei = id) #get the manuscript that you want to output
	FullText = "" #set fulltext as empty string
	AllPages = Page.objects.filter(id_tei__contains = id) #get all pages that are in the manuscript
	for i in range(0,len(AllPages)):
		FullText = FullText + AllPages[i].fulltext + " "#add all text to FullText
	s = MLStripper()
	s.feed(FullText)
	newtext = s.get_data() #remove all HTML from text
	response = HttpResponse(newtext, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename="%s.txt"' % ManuToOutput.id_tei
	return response

def outputAll(request):
	#use for loops to get info of each manuscript
	f = cs.StringIO() # or a file on disk in write-mode
	zf = z.ZipFile(f, 'w', z.ZIP_DEFLATED)
	Manuscripts = Manuscript.objects.all()
	ListOfManuscripts = []
	for i in range (0,len(Manuscripts)):
		Pages = Page.objects.filter(id_tei__contains = Manuscripts[i].id_tei)
		FullText = ""
		for j in range(0,len(Pages)):
			FullText = FullText + Pages[j].fulltext + " "
		s = MLStripper()
		s.feed(FullText)
		newtext = s.get_data() #remove all HTML from text
		ListOfManuscripts = ListOfManuscripts + [[newtext,Manuscripts[i].id_tei]] #Add full text to list of full texts
	for k in range(0,len(ListOfManuscripts)):
		response= HttpResponse(ListOfManuscripts[k][0],content_type='text/plain')
		response['Content-Disposition'] = 'attachment; filename="%s.txt"' % ListOfManuscripts[k][1]
		#zf.write('sample.txt)
	#zf.close()
	return response

def manu_detail(request,id):
	try:
		manu = Manuscript.objects.get(id_tei = id) #get this manuscript!
	except Manuscript.DoesNotExist:
		raise Http404('this manuscript does not exist')
	allpages = Page.objects.filter(id_tei__contains = manu.id_tei) #get all pages from this manuscript!
	Space = str(manu.person_id).index(" ")
	TrueAuthor = str(manu.person_id)[0:Space] #find the author ID of this person
	Author = Person.objects.get(id_tei=TrueAuthor) #get the actual person
	return render(request,'manu_detail.html', {'manu':manu,'allpages':allpages, 'Author':Author
	})

def person_detail(request,id):
	try:
		person = Person.objects.get(id_tei = id)
	except Person.DoesNotExist:
		raise Http404('this person does not exist')
	allpages = Page.objects.filter(fulltext__contains = id) #list of pages containing this person
	manuscripttitles = [] #make a list of all manuscript titles that are relevant (in for loop)
	for i in range(0,len(allpages)):
		manuscripttitles = manuscripttitles + [allpages[i].Manuscript_id]
	allmanuscripts = Manuscript.objects.filter(title__in = manuscripttitles) #get list of these manuscripts from the title list
	# ^ this should collect all relevant manuscripts
	""" the following lines are about finding the correct birth place & death place """
	#checking if the birth place is mud creek because right now mud creek doesn't have an ID_TEI
	newBP = str(person.birth_place)
	if 'Mud Creek' in newBP:
		MC = 'True'
	else:
		MC = 'False'
	#checking if the death place is mud creek because right now mud creek doesn't have an ID_TEI
	newDP = str(person.death_place)
	if 'Mud Creek' in newDP:
		MC1 = 'True'
	else:
		MC1 = 'False'
	#now, if birth place & death place aren't mud creek, let's get their id's!
	if MC == 'False':
		FirstSpace = newBP.index(' ') #find first space in birth place
		newbirthplace = newBP[0:FirstSpace] #get the id_tei of the birth place
		birthplace = Place.objects.get(id_tei = newbirthplace) #get the real birth place! (via model)
	else:
		birthplace = "Mud Creek"
	#/////////////
	if MC1 == 'False':
		FirstSpace1 = newDP.index(' ')
		newdeathplace = newDP[0:FirstSpace1] #get id_tei of death place
		deathplace = Place.objects.get(id_tei = newdeathplace) #get real death place (via model)
	else:
		deathplace = "Mud Creek"
	""" Done finding death place & birth place """
	#Now, find proper names of all the affiliations!
	newAffiliations = []
	for i in range(0,len(person.affiliations.all())):
		FS = str(person.affiliations.all()[i]).index(' ') #locate first space
		newAff = str(person.affiliations.all()[i])[0:FS] #find id_tei of affiliation (aka group)
		newAff1 = Org.objects.get(id_tei = newAff) #find instance of group model!
		newAffiliations = newAffiliations + [newAff1] #add to list of Affiliations!
	return render(request,'person_detail.html',{
	'person':person, 'allpages':allpages, 'allmanuscripts':allmanuscripts, 'MC':MC,'MC1':MC1,'birthplace':birthplace,'deathplace':deathplace, 'newAffiliations':newAffiliations
	})

def place_detail(request,id):
	try:
		place = Place.objects.get(id_tei = id)
	except Place.DoesNotExist:
		raise Http404('this place does not exist')
	allpages = Page.objects.filter(fulltext__contains = id) #list of pages containing this Place
	manuscripttitles = [] #make a list of all manuscript titles that are relevant
	for i in range(0,len(allpages)):
		manuscripttitles = manuscripttitles + [allpages[i].Manuscript_id]
	allmanuscripts = Manuscript.objects.filter(title__in = manuscripttitles)
	#this should collect all relevant manuscripts
	return render(request,'place_detail.html',{
	'place':place, 'allpages':allpages, 'allmanuscripts':allmanuscripts
	})

def org_detail(request,id):
	try:
		org = Org.objects.get(id_tei = id)
		#place = Place.objects.get(id_tei = org.place_id)
	except Org.DoesNotExist:
		raise Http404('this organization does not exist')
	allpages = Page.objects.filter(fulltext__contains = id) #list of pages containing this Org
	manuscripttitles = [] #make a list of all manuscript titles that are relevant
	for i in range(0,len(allpages)):
		manuscripttitles = manuscripttitles + [allpages[i].Manuscript_id]
	allmanuscripts = Manuscript.objects.filter(title__in = manuscripttitles)
	#this should collect all relevant manuscripts
	return render(request,'org_detail.html',{
	'org':org, 'allpages':allpages, 'allmanuscripts':allmanuscripts,
	#'place':place
	})


def pageinfo(request,id):
	try:
		page = Page.objects.get(id_tei = id)
		manuscript = Manuscript.objects.get(title = page.Manuscript_id)
	except Page.DoesNotExist:
		raise Http404('this page does not exist')
	#need to go through manuscript pages and determine which is the last page
	j=0
	for i in range(1,1000): # i made this range bc page # is in 000 format so 999 should b highest # page possible
		# page_id will be manuscript_id + _ + i
		try:
			if i < 10:
				pageid = manuscript.id_tei + "_00" + str(i)
			elif i < 100:
				pageid = manuscript.id_tei + "_0" + str(i)
			else:
				pageid = manuscript.id_tei + "_" + str(i)
			testpage = Page.objects.get(id_tei = pageid)
		except:
			if j==0:
				j=j+1 #make sure this only happens the first time that the "except" is reached
				lastpage = i-1
 	#now lastpage should be the page number of the last page in the manuscript!
	Page_id = id[len(id)-3:] # this should be the page #
	return render(request,'page_detail.html', {
	'page':page,'manuscript':manuscript, 'lastpage':lastpage, 'Page_id':Page_id
	})

	#gotta include info as to whether or not it's the first or last pg in a manuscript!

def newpageinfo(request,id): #for when cornplanter.js tries to get info of a new page
		try:
			page = Page.objects.get(id_tei = id)
			manuscript = Manuscript.objects.get(title = page.Manuscript_id)
		except Page.DoesNotExist:
			raise Http404('this page does not exist')
		#need to go through manuscript pages and determine which is the last page
		j=0
		for i in range(1,1000): # i made this range bc page # is in 000 format so 999 should b highest # page possible
			# page_id will be manuscript_id + _ + i
			try:
				if i < 10:
					pageid = manuscript.id_tei + "_00" + str(i)
				elif i < 100:
					pageid = manuscript.id_tei + "_0" + str(i)
				else:
					pageid = manuscript.id_tei + "_" + str(i)
				testpage = Page.objects.get(id_tei = pageid)
			except:
				if j==0:
					j=j+1 #make sure this only happens the first time that the "except" is reached
					lastpage = i-1
	 	#now lastpage should be the page number of the last page in the manuscript!
		Page_id = id[len(id)-3:] # this should be the page #
		return render(request,'page_detail_2.html', {
		'page':page,'manuscript':manuscript, 'lastpage':lastpage, 'Page_id':Page_id
		})

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

def jsoninfo(request,id): #this is where the side tab gets its info on the page viewer!
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


def storymap(request, xml_id):
	return render(request, 'story_maps/' + xml_id + '.html')

def travelRoutes(request):
	return render(request, 'travelRoutes.html')
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
