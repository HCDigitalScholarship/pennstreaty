
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from django.template.loader import get_template
from django.shortcuts import render, render_to_response, redirect
from django.core import management, serializers
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Person, Place, Org, Relationship, Page, Manuscript, PendingTranscription
from html.parser import HTMLParser
import zipfile as z

from io import StringIO as cs

from tempfile import *
from .forms import ContactForm, ImportXMLForm, TranscribeForm
from django.core.mail import EmailMessage, send_mail
from django.views.generic import ListView, DetailView
from .xml_import import import_xml_from_file

from django.urls import reverse

import difflib
import os
import cgi

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

class Home(TemplateView):
    template_name = 'index.html'

def testing(request):
    return render(request, 'review_transcription.html')

def contact(request):
    form_class = ContactForm
    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
                contact_name = request.POST.get('contact_name', '')
                contact_email = request.POST.get('contact_email', '')
                form_content = request.POST.get('content', '')
        # Email the profile with the contact information
                template = get_template('contact_template.txt')
                context = Context({'contact_name': contact_name,
                                   'contact_email': contact_email,
                                   'form_content': form_content})
                content = template.render(context)
                send_mail("New contact form submission from "+contact_name,content,contact_email,['hcdigitalscholarship@gmail.com'],fail_silently=False,)
                return redirect('contactSuccess') #this redirects to contactpage , should go somewhere else?
    return render(request, 'contact.html', {'form': form_class})

def contactSuccess(request):
    return render(request, 'contactSuccess.html')

def about(request):
    return render(request, 'about.html')

def mapgallery(request):
    return render(request, 'mapgallery.html')

def historicalbackground (request):
    return render(request, 'historicalbackground.html')

def manuscripts(request):
    textlist = Manuscript.objects.filter(transcribed=True).order_by('title')
    pagelist = Page.objects.order_by('Manuscript_id')
    return render(request, 'manuscripts.html', {'textlist':textlist,'pagelist':pagelist})
def transcribe(request):
    textlist = Manuscript.objects.filter(transcribed=False).order_by('title')
    pagelist = Page.objects.order_by('Manuscript_id')
    return render(request, 'transcribe.html', {'textlist':textlist,'pagelist':pagelist})
def profiles(request):
    person_list = Person.objects.order_by('last_name')
    place_list = Place.objects.order_by('name')
    org_list = Org.objects.order_by('organization_name')
    return render(request, 'profiles.html', {'persons': person_list, 'places': place_list, 'orgs': org_list})

def base(request): 
	return render(request, 'base.html')
	
def base_explicit(request): 
	return render(request, 'base_explicit.html')
	
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
    response = render_to_response('detail.html', {}, context_instance=RequestContext(request))
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
    response['Content-Disposition'] = 'attachment; filename="%s.pdf"'% PageToOutput.id_tei
    buffer = BytesIO()
    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(30, 750, "Hello World")
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
        super().__init__()
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
    for i in range(0, len(AllPages)):
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
    search_term=""

    try:
        manu = Manuscript.objects.get(id_tei = id) #get this manuscript!
    except Manuscript.DoesNotExist:
        raise Http404('this manuscript does not exist')
    allpages = Page.objects.filter(id_tei__contains = manu.id_tei) #get all pages from this manuscript!
    newpages = []
    for page in allpages:
        newpages += [page]
    allpages = sorted(newpages,key=lambda x: x.id_tei)

    return render(request,'manu_nav.html', {'manu':manu,'allpages':allpages, 'search_term':search_term})

"""
    if 'search' in request.GET:
       search_term = request.GET['search']
       page=page.filter(fulltext__icontains=search_term)
"""


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
    #Now, find proper names of all the affiliations!
    newAffiliations = []
    for i in range(0,len(person.affiliations.all())):
        FS = str(person.affiliations.all()[i]).index(' ') #locate first space
        newAff = str(person.affiliations.all()[i])[0:FS] #find id_tei of affiliation (aka group)
        newAff1 = Org.objects.get(id_tei = newAff) #find instance of group model!
        newAffiliations = newAffiliations + [newAff1] #add to list of Affiliations!
    return render(request,'person_detail.html',{
    'person':person, 'allpages':allpages, 'allmanuscripts':allmanuscripts,'newAffiliations':newAffiliations
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



def transcribe_info(request,id):
    try:
       current_page = Page.objects.get(id_tei = id)
       manuscript = Manuscript.objects.get(title = current_page.Manuscript_id)
    except Page.DoesNotExist:
       raise Http404('this page does not exist')
    j = 0
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
    pagenumber = int(Page_id)
    
    Manuscript_key = current_page.Manuscript_id
    possible_pages = Page.objects.filter(Manuscript_id = Manuscript_key)
    pages_list=[]
    for index, page in enumerate(possible_pages):
        pages_list.append(page)

        if page == current_page:
                print('current=', index)
                current = int(index)
    previous = pages_list[current-1]
    try:
        next_one = pages_list[current+1]
    except:
        next_one = pages_list[0]

    total = len(possible_pages)
    #message = 'Your submission encountered errors, please contact us'
    message = 'Your transcription has already been successfully submitted for approval!'
    if request.method == 'POST':
        form = TranscribeForm(request.POST)
        if form.is_valid():
            # Replace newlines with <br> tags and escape all HTML tags.
           clean_text = '<br>'.join(cgi.escape(form.cleaned_data['text']).splitlines())
           clean_author = cgi.escape(form.cleaned_data['name'])
           current_page.pendingtranscription_set.create(transcription=clean_text, author=clean_author)
           #message = 'Your transcription has already been successfully submitted for approval!'
    else:
       form = TranscribeForm(initial={'text': current_page.fulltext, 'name':''})
    return render(request,'transcribe_detail.html', {'message':message, 'current_page':current_page,'manuscript':manuscript, 'lastpage':lastpage, 'Page_id':Page_id, 'form':form, 'previous':previous, 'next_one':next_one, 'total':total, 'Page_id':Page_id, 'pagenumber': pagenumber})


def pageinfo(request,id):
    try:
        current_page = Page.objects.get(id_tei = id)
        manuscript = Manuscript.objects.get(title = current_page.Manuscript_id)
    except Page.DoesNotExist:
        raise Http404('this page does not exist')
    # need to go through manuscript pages and determine which is the last page
    j = 0
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

    pagenumber = int(Page_id)
    
    Manuscript_key = current_page.Manuscript_id
    possible_pages = Page.objects.filter(Manuscript_id = Manuscript_key)
    pages_list=[]
    for index, page in enumerate(possible_pages):
        pages_list.append(page)

        if page == current_page:
                print('current=', index)
                current = int(index)
    previous = pages_list[current-1]
    try:
        next_one = pages_list[current+1]
    except:
        next_one = pages_list[0]

    total = len(possible_pages)
    
    query = request.GET.get("q")

    search_result=[]
    if query:
       search_result = possible_pages.filter(fulltext__icontains=query)

    template_name='viewpage.html'   
    return render(request,template_name, {'search_result': search_result, 'current_page':current_page,'manuscript':manuscript, 'lastpage':lastpage, 'Page_id':Page_id, 'total':total, 'previous':previous, 'next_one':next_one,'pagenumber':pagenumber})

	#gotta include info as to whether or not it's the first or last pg in a manuscript!

def page_Redirect(request,page):
    args=['page',page]
    return HttpsResponseRedirect(reverse('QI:viewpage2',args=args))

def newpageinfo(request,id): #for when cornplanter.js tries to get info of a new page
    try:
        page = Page.objects.get(id_tei = id)
        manuscript = Manuscript.objects.get(title = page.Manuscript_id)
    except Page.DoesNotExist:
        raise Http404('this page does not exist')
    #need to go through manuscript pages and determine which is the last page
    j = 0
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

def pagetranscription(request,id):
    try:
        page = Page.objects.get(id_tei = id)
        manuscript = Manuscript.objects.get(title = page.Manuscript_id)
    except Page.DoesNotExist:
        raise Http404('this page does not exist')
    #need to go through manuscript pages and determine which is the last page
    j = 0
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
    return HttpResponse(page.fulltext)

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
    return render(request, 'test.html', {'orgs':orgs,'persons':persons,'places':places})

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
            if char != '.':
                trunc_fileName=trunc_fileName+char
            else:
                afterdot=True
                continue
        if fileType != "xml":
            print ("Needs to be a .xml file")
            #it would be sick if a had an error message or page
            return render(request, '../templates/admin/SMimport/index.html',{'failed' : True})
        print (fileType)
        print (trunc_fileName)
        print (fileName)
        print ('/static/xml/'+fileName)
        #This is pretttty hacky and may have some problems
        #I am changing the working directory so that python writes it into the spot I want it to
        #Is there a better way to do this? Probably. Can probably do it where you open the file, but that wasn't working for me
        current_directory=os.getcwd()
        print (current_directory, type(current_directory))
        os.chdir(current_directory+"/static/xml")
        print (os.getcwd())
        with open(fileName,'w') as f:
            print ("we did it")
            a=the_file.read()
            #print a
            f.write(a)
        os.chdir(current_directory)
        management.call_command('generate',trunc_fileName)
        return render(request, '../templates/admin/SMimport/index.html',{"success" : True})
    else:
        return render(request, '../templates/admin/SMimport/index.html')


def new_xml_import(request):
    if request.method == 'POST':
        form = ImportXMLForm(request.POST, request.FILES)
        if form.is_valid():
            import_xml_from_file(request.FILES['xml_file'])
        context = {'success': True, 'form': ImportXMLForm()}
        return render(request, '../templates/admin/XMLimport/index.html', context)
    else:
        form = ImportXMLForm()
    return render(request, '../templates/admin/XMLimport/index.html', {'form': form})


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
            if char != '.':
                trunc_fileName=trunc_fileName+char
            else:
                afterdot=True
                continue
        if fileType != "xml":
            print ("Needs to be a .xml file")
            #it would be sick if a had an error message or page
            return render(request, '../templates/admin/XMLimport/index.html',{'failed' : True})
        print (fileType)
        print (trunc_fileName)
        print (fileName)
        print ('/static/xml/'+fileName)

        #This is pretttty hacky and may have some problems
        #I am changing the working directory so that python writes it into the spot I want it to
        #Is there a better way to do this? Probably. Can probably do it where you open the file, but that wasn't working for me
        current_directory=os.getcwd()
        print (current_directory, type(current_directory))
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


def review_transcription(request, pk):
    obj = PendingTranscription.objects.get(pk=pk)
    #looking for primary key
    if request.method == 'POST':
        if 'deletebutton' in request.POST:
            obj.delete()
            messages.success(request, 'The transcription was successfully deleted.')
        else:
            obj.doc.fulltext = obj.transcription
            obj.doc_transcribed = False
            obj.doc.Manuscript_id.transcribed = True 
            obj.doc.save()
            obj.delete()
            messages.success(request, 'The transcription was successfully approved.')
        return HttpResponseRedirect('/admin')
    else:
        old_lines = split_html_lines(obj.doc.fulltext)
        new_lines = split_html_lines(obj.transcription)
        d = difflib.Differ()
        diff_lines = list(d.compare(old_lines, new_lines))
        for i, line in enumerate(diff_lines):
            if line.startswith('  '):
               diff_lines[i] = '<span class="diff-both">' + line[2:] + '</span>'
            elif line.startswith('- '):
               diff_lines[i] = '<span class="diff-first">' + line[2:] + '</span>'
            elif line.startswith('+ '):
               diff_lines[i] = '<span class="diff-second">' + line[2:] + '</span>'
            elif line.startswith('? '):
                diff_lines[i] = '<span class="diff-neither">' + line[2:] + '</span>'
        context = {
            'object': obj,
            'diff_table': '<br>'.join(diff_lines)
        }
        #Page_id = id[len(id)-3:]
        return render(request, 'review_transcription.html', context)

def split_html_lines(html_str):
    # New transcriptions will always insert '<br>', but some of the old transcriptions have variant
    # spellings of the tag.
    html_str = html_str.replace('<br/>', '<br>').replace('<br />', '<br>')
    return html_str.split('<br>')

class ReviewTranscriptionList(ListView):
    model = PendingTranscription
    template_name = 'review_transcription_list.html'


def inText_search(request):
    query = request.GET.get("q")
    return render(request, "search/inText_search.html")

