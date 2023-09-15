from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


from PIL import Image
import os
os.system('rm /tmp/*.pdf') # deletes all the pdfs in /tmp/, so don't store any important PDFs there!
import datetime

from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
import lxml

from QI.models import Manuscript, Page

class Command(BaseCommand):
        help = "generate PDFs for all Manuscripts"
        def add_arguments(self, parser):
        	parser.add_argument('ID_TEI')


        def handle(self, *args, **options):
        	    buff=build(options['ID_TEI'])
#def get_id_tei(document):
   # id_tei=document.id_tei
    #return id_tei

def get_all_pages(document):
    title=document.title
    all_pages = Page.objects.filter(Manuscript_id__title=title)
    return all_pages

def get_image_path(page):
    prefix='/app/media/img/'
    suffix='.jpg'
    image_path=prefix+page.id_tei+suffix
    print (image_path)
    return image_path


fields_in_display_order= ['id_tei','type_of_Manuscript', 'call_no','date','location','author','summary']
fields=['id_tei','type_of_Manuscript', 'call_no','date','location','person_name','org_name','summary']

def get_metadata(document):
    metadata = {}
    labels = {}
    for field in fields:
        metadata[field] = getattr(document,field) if hasattr(document,field) else None
    labels['title'] = 'Title'
    labels['id_tei'] = "TEI ID"
    labels['type_of_Manuscript'] = 'Manuscript Type'
    labels['call_no'] = 'Call Number'
    labels['date'] = 'Date'
    labels['location'] = 'Location'
    labels['summary'] = 'Summary'
    labels['author'] = "Author(s)"
    return labels,metadata

def split(tittle):
    words=tittle.split()
    firstline=""
    i=0
    while i<=10:
        firstline=firstline+words[i]+" "
        i+= 1
    secondline=""
    while i<len(words):
        secondline=secondline+words[i]+" "
        i+= 1
    
    return firstline,secondline

def break_texts_to_lines(texts):
    words=texts.split()
    words_count=len(words)
    print (words_count)
    big_loop_count=int(len(words)/10)+1
    print (big_loop_count)
    k=1
    lines=[]
    while k <= big_loop_count:
        line=""
        i=0
        if k == big_loop_count:
            while i < len(words):
                line=line+words[i]+" " 
                i += 1   
            print(line)
            lines.append(line)
        else:
            while i < 10:
                line=line+words[i]+" "
                i+= 1
            print(line)
            lines.append(line)
            words=words[i:]
        k += 1
    return lines    
     

class PageNumCanvas(canvas.Canvas):
        def __init__(self,*args,**kwargs):
                canvas.Canvas.__init__(self, *args, **kwargs)
                self.pages = []

        def showPage(self):
                """
                On a page break, add information to the list
                """
                self.pages.append(dict(self.__dict__))
                self._startPage()
        def save(self):
                """
                Add the page number to each page (page x of y)
                """
                page_count = len(self.pages)

                for page in self.pages:
                        self.__dict__.update(page)
                        #self.draw_page_number(page_count)
                        canvas.Canvas.showPage(self)
                canvas.Canvas.save(self)
#        def draw_page_number(self,page_count):
                #self.setFont('Georgia',12)
#                self.drawCentredString(4.25*inch,.25*inch+32,'https://pennstreaty.haverford.edu/manuscripts/ - page %s of %s' % (str(self._pageNumber),str(page_count)))
#                canvas.Canvas.save(self)

def build(TEI_ID):
    response= '/tmp/%s.pdf' % TEI_ID
    document = Manuscript.objects.get(id_tei=TEI_ID)
    page_num = 1
    labels, metadata = get_metadata(document)

    canv = PageNumCanvas(response, pagesize = letter, bottomup = 1)
    title= "Beyond Penn's Treaty" + "/"+TEI_ID
    canv.setTitle(title)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    canv.drawImage('/app/media/img/PennsTreaty-West2.jpg', 0.000001*inch, 8.9*inch, 8.6*inch, 2.6*inch)
    canv.setFillColorRGB(255,255,255)
    canv.setFont("Times-BoldItalic",35)
    canv.drawString(0.1*inch,9.1*inch,"Beyond Penn's Treaty")
    canv.setFillColorRGB(0,0,0)
    canv.setFont("Times-Italic",18)
    words=document.title.split()
    if len(words)>10:
        firstline,secondline=split(document.title)
        canv.drawCentredString(4.25*inch,8.2*inch,firstline)
        canv.drawCentredString(4.25*inch,7.95*inch,secondline)
    else:
        canv.drawCentredString(4.25*inch,8.2*inch,document.title)

    #canv.setFont("Courier-BoldOblique",14)
    #canv.drawString(1*inch,7.8*inch,"Metadata")
    metadata_text = canv.beginText()
    metadata_text.setTextOrigin(inch, 7.5*inch)
    for field in fields_in_display_order:#field (Authors) and Summary are special
        metadata_text.setFont("Helvetica", 10)
        label=field.upper() + ':'
        metadata_text.textOut(label)
        metadata_text.moveCursor(2*inch, 0)
        metadata_text.setFont("Times-Roman", 13)
        if field == "summary":
            try:
                info = metadata[field]
                summary_lines=break_texts_to_lines(metadata['summary'])
                for line in summary_lines:
                    metadata_text.textOut(line)
                    metadata_text.moveCursor(0,14)
            except ValueError:
                pass
        elif field == "author":
            try:
                info = metadata["person_name"]
                metadata_text.textOut(info)
       #         metadata_text.moveCursor(0,16)
            except ValueError:
                info = metadata["org_name"]
                metadata_text.textOut(info)
       #         metadata_text.moveCursor(0,16)           
        else:
            try:
                info = metadata[field]
                metadata_text.textOut(info)
       #         metadata_text.moveCursor(0,16)
            except ValueError:
                print('unable to find %s for document %s.' % (field,document.id_tei))
        metadata_text.moveCursor(-2*inch, 20)
       
#    metadata_text.setFont('Georgia-Italic',12)
    metadata_text.textOut('How to cite:')
    now = datetime.datetime.now().strftime('%a %d %b %Y %I:%M %p EST')
    metadata_text.textOut('Accessed online ' + now)
    canv.drawText(metadata_text)
    canv.showPage()

    canv.drawCentredString(4.25*inch,8.5*inch,"This page is intentionaly left as blank.")
    canv.showPage()


    for page in get_all_pages(document):
        
        image_path=get_image_path(page)
        try:
            #image_page= canv.beginText()
            #image_page.setTextOrigin(inch,10*inch)
            image=ImageReader(image_path)
            #image_page.textOut(image_path)
            #canv.drawText(image_page)
            canv.drawImage(image, 0.35*inch, 0, 7.57*inch, 11*inch)
            canv.showPage()
        except OSError:
             pass

        soup = BeautifulSoup(page.fulltext,'lxml')
        prettysoup=soup.prettify()
        print("soup type", type(soup))
        print("soup", soup)
        print("prettysoup", prettysoup)
        for lb in soup.findAll('br'):
            lb.replaceWith('n1')
        #for p in soup.body.div.findAll('p'):
            #print("p is", p)
            #paratext=str(p)
            #paratext=paratext.replace("<p class="tei-text">","\n")
            #p.replacewith('gug')
     
#this is a trick I use because I don't really understand how beautiful soup tackle parsing xml esepcially about line breaks.
#Somehow there are mysterious '\n' breaks already besides those encode by <br>s or <lb>s. An these '\n' tags do not match with
#the line breaks on the images

        transcription_text = canv.beginText()
        transcription_text.setTextOrigin(inch,10*inch)
        transcription_text.textOut('Transcription')
        transcription_text.moveCursor(0,40)
        transcription_text.setFont('Times-Roman', 12)
        text=soup.get_text()
        text=text.replace('Person Information ','')
        text=text.replace('Place Information','')
        text=text.replace('Organization Information','')
        text=text.replace("                    ","")
        text=text.replace('\n',"ytf ")
        text=text.replace('n1', '\n')
        print("text:", text)
        text_lines = [line for line in text.split('\n') if line != '']
        for i in range(len(text_lines)):
            print("line:",text_lines[i])
            transcription_text.textOut(text_lines[i])
            transcription_text.moveCursor(0,13)

        canv.drawText(transcription_text)
        canv.showPage()
    canv.save()
