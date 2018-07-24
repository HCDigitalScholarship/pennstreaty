
from django.core.management.base import BaseCommand, CommandError

#1
import os
from xml.etree.ElementTree import ElementTree

from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import json
import xlrd
from QI.models import Place
from bs4 import BeautifulSoup


class Command(BaseCommand): #2
	args = 'Arguments is not needed'
	help = 'Django admin custom command'
	
	def add_arguments(self, parser):
		parser.add_argument('xml_file', nargs='+', type=str)
	
	
	def handle(self, *args, **options):
		for xml_file in options['xml_file']: #3
		#this for loop allows you generate storymaps for multiple xml files by running python manage.py generate file1 file2
			#4
			file_name = 'static/xml/' + xml_file + '.xml'
			workbook = xlrd.open_workbook('static/xls/TEI people, places, orgs.xlsx')#LOCATION
			worksheet = workbook.sheet_by_name('Places')#LOCATION
			tree = etree.parse(file_name)
			root = tree.getroot() 

			ns = ""
			if root.tag[0] == "{":
				x = 1
				ns = root.tag[0]
			while root.tag[x-1] != "}":
				ns += root.tag[x]
				x += 1
			#line 35-41 are necesssary to keep, although I don't understand what id namespace here. It is inherited from old version of generate.py 	

			title = ""
			titlelist =[]
			for a in root.iter(ns + "titleStmt"):
				titlelist.append(a)
			if len(titlelist)>0:
				for x in root.iter(ns + "titleStmt"):
					for child in x:
						if child.tag == ns + "title":
							title = child.text
							#get node value under "<title>"
			title_fin = title
			if title.endswith("Version"):
				title_fin = title_fin.replace("\n","")
				title_fin = title_fin.replace("Version", "")
				title_fin = title_fin.replace("Electronic","")
				title_fin = title_fin.replace(": ", "")
				title_fin = title_fin.replace("  ","")
				#delete ":Electronic:Version" from the text under <title> in xml
			print (title_fin)
			#7

			description = ""
			desc_list = []
			for b in root.iter(ns + "projectDesc"):
				desc_list.append(b)
			if len(desc_list)>0:
				for b in root.iter(ns + "projectDesc"):
					for child in b:
						if child.tag == ns + "p":
							description = child.text	
			print (description[:100]+"...")

			entries = []
			for div in root.iter(ns + 'div'):
				if div.get('type') == 'entry':
					entries.append(div)
			print (entries)
			# storymap only create slides for "type=entry". We get all divs with"type = entry" first.

			objects = []# createing a list that will hold each slides of storymap, and this object is stored as json at last
			pages = []# hold page numbers for image caption later
			tei_ids=[]# hold tei_id to create img_url
			for f, e in enumerate(entries):
				#f is intger, e are 'div type=entry' elements
				div_text = ""

				for child in e:
					if child.tag == ns + 'p':
					 #each entry contains multiple "<p>", iterate within one entry to get all text
						text = etree.tostring(child, method='text')
						#tostring method will convert xml to string, but it will keep some tags
						text = text.decode('utf-8')
						text = text.replace('\n', '')
						text = text.replace('\\xe2\\x80\\x94','-')
						text = text.replace('\\xe2\\x80\\x99',"'")
						# line 94-97 take out tags and replace some of unicode characters
						div_text = div_text+text

						for subelement in child:
							if subelement.tag == ns + 'pb':
								page = subelement.get('n')
								tei_id = subelement.get('facs')#use 'facs' value to get tei_id. There are issues with this. Read wiki
								pages.append(page)
								tei_ids.append(tei_id)

					if child.tag == ns + "dateline":
						# <dateline><date when="xxx">xxx</date>.<placeName key="zz">yyy</placeName></dateline>, we can get date and place in <dateline> element
						dateline = child
						for child in dateline:
							if child.tag == ns + "placeName":
								place = child.get("key")
							if child.tag == ns + "date":
								date = child.get("when")
				#print ('div_text is:', div_text)
				print ('last page in pages is: ', pages[-1:])
				print ('last tei_id in pages is: ', tei_ids[-1:])

				
				img_caption = page_repr(pages[-1:])
				img_url = media_url_repr(tei_ids[-1:])
				print ('img_caption after loop:', img_caption)
				print ('img_url after loop:', img_url)
				
				#get a list of place(should be one place only) in this entry
				dj_place_list = Place.objects.filter(id_tei=place)
				print ("dj_place_list:: \n", dj_place_list, len(dj_place_list))
				

				if dj_place_list==None or dj_place_list==list() or len(dj_place_list)==0: 
				#check if places from the manuscript are in database			
					print (place, "not found in database \n")
					continue

				else:
					for i in dj_place_list:
						if i.latitude != None:
							dj_place = i 
							break
							 #if it passes the if statement, skip the loop 
						else:
							dj_place = i
							print ("i.latitude is 'None'")

					lat = dj_place.latitude
					lon = dj_place.longitude

					if lat =="" or lon== "":
						print ("No lat or lon for",place,"I set this to lat to 42 and lon to 83. \n")
						lat = 42 #LOCATION
						lon = 83#LOCATION
					else:
						print (place, "had lat, lon:",lat,lon,"\n")
					try:
						float(lat)
					except ValueError:
						print ("People are bad at entering data, lat for this is:", lat)
						lat = 42
						print ("set lat to 42")
					try:
						float(lon)
					except ValueError:
						print ("People are bad at entering data, lon for this is:", lon)
						lon = 83
						print ("set lon to 83")			
				#Important: the spreadsheet is North and West, so you have to make it negative if you dont want to end up in Tajikistan
				object = {"location":{'lat':float(lat), 'lon':-float(lon)}, "text":{"headline":date_repr(date), "text":div_text},"media":{"url":img_url,"caption":img_caption}}
				objects.append(object)

			cover = {"type":"overview", "text":{"headline":title_fin, "text":description}}
			objects.insert(0, cover)

			map = {"calculate_zoom":False, "storymap":{"call_to_action":True, "map_type":"statemen:toner-lite","map_as_image":False, "slides":objects}}
			data = map
			
			#write json data into a json dile 
			with open('static/json/' + xml_file + '.json', 'w') as outfile:
				json.dump(data, outfile, sort_keys=True)
			
			#write html template for the storymap
			html_str = """{% load staticfiles %}
			<!doctype html>
<html class="no-js" lang="en">
  <head>
    {% include 'top-links.html' %}
    <title>"""+ xml_file + """ StoryMapJS </title>
    <link rel="stylesheet" href="https://cdn.knightlab.com/libs/storymapjs/latest/css/storymap.css">
    
  </head>
  <body>
	{% include 'header.html' %}
   <div id = "row1">
  <!--     Navigation Menu Below:  -->
    {% include 'nav.html' %}
  </div>
	<div id = "story1" style = "background-color: #F0F8FF;">
	   <div>
	      <br />
	      <h2 class = "text-center" style = "font-family: 'Alegreya Sans SC'; font-weight: 400; color: black"> StoryMap for """+ xml_file + """</h2>
	        <!-- The StoryMap container can go anywhere on the page. Be sure to 
    specify a width and height.  The width can be absolute (in pixels) or 
    relative (in percentage), but the height must be an absolute value.  
    Of course, you can specify width and height with CSS instead -->
    <div id="mapdiv" style="width: 90%; height: 600px; margin:auto"></div> 
    <br />
    <br />
	  </div>  
	</div>
  	{% include 'footer.html' %}
    
 {% include 'bottom-links.html' %}
  <!-- Your script tags should be placed before the closing body tag. -->
    <script type="text/javascript" src="https://cdn.knightlab.com/libs/storymapjs/latest/js/storymap-min.js"></script>
     <script>
  // storymap_data can be an URL or a Javascript object
 
      //var storymap_data = "{% static "json/StoryMapData.json" %}"; 
      var storymap_data = "{% static "json/""" + xml_file + """.json" %}"; 
      
      // certain settings must be passed within a separate options object
      var storymap_options = {};
      var storymap = new VCO.StoryMap('mapdiv', storymap_data, storymap_options);
      window.onresize = function(event) {
          storymap.updateDisplay(); // this isn't automatic
      }          
  </script>
  
  
  </body>
</html>""" 
			html_file = open('templates/story_maps'+xml_file+'.html','w')
			html_file.write(html_str)
			html_file.close()
			#create html template

			#adds to list of xml ids to be made into urls
			file_names = 'static/xml/xml_file_names.xml'
			tree = etree.parse(file_names)
			root = tree.getroot()
			list_of_files=[]
			for child in root:
				list_of_files.append(child.text)

			new_file = False

			if xml_file not in list_of_files:
				x = etree.SubElement(root,'file')
				x.text = xml_file
				tree.write('static/xml/xml_file_names.xml')
				new_file = True
			#to check if this storymap has already existed	
			#new_file = "True"#delete this when I am done with storymap!!!!

			if new_file:
				#if it is a new file, we need to make a link to it on 'list_of_storymap.html'.
				newfile=""
				with open('templates/list_of_storymaps.html', 'r+') as f:
					html_as_string=f.read()
					
					soup = BeautifulSoup(html_as_string, 'html.parser')
					#BeaurifulSoup is a tool that parser html
					sml = soup.find(id='storymaplist')
					links = soup.find_all('a')
					newtag= soup.new_tag('a', id='SMLink', href=xml_file)
					atag= soup.new_tag('a', href=xml_file)
					imgtag= soup.new_tag('img', src='../static/img/'+xml_file+'1797.jpg')
					#url in line 267 need to be replaced with correct url manually in list_of_storymaps.html
					litag = soup.new_tag('li', id='SMListitem')
					divtag = soup.new_tag('div', id="SMtext")
					divtagimg = soup.new_tag('div', id="SMimgdiv")
					soup.ul.append(litag)
					litag.append(atag)
					atag.append(divtagimg)
					divtagimg.append(imgtag)
					atag.append(divtag)
					divtag.append(newtag)
					newtag.string = title_fin

					newfile = soup.prettify()
					print(newfile[-300:])
					#turn a Beautiful Soup parse tree into a nicely formatted Unicode string, with each HTML/XML tag on its own line:
				with open('templates/list_of_storymaps.html','w') as f:
					f.write(newfile)



def date_repr(date_str):
	#ex: "1793-07-20"
	#want to be : "July 20, 1793"
	year = date_str[0:4]
	day = date_str[-2:]
	month = date_str[5:7]
	if month == "01":
		mo_fin = "January"
	elif month == "02":
		mo_fin = "February"
	elif month == "03":
		mo_fin = "March"
	elif month == "04":
		mo_fin = "April"
	elif month == "05":
		mo_fin = "May"
	elif month == "06":
		mo_fin = "June"
	elif month == "07":
		mo_fin = "July"
	elif month == "08":
		mo_fin = "August"
	elif month == "09":
		mo_fin = "September"
	elif month == "10":
		mo_fin = "October"
	elif month == "11":
		mo_fin = "November"
	else:
		mo_fin = "December"
	return mo_fin + " " + day +", " +year#20

def media_url_repr(tei_ids_list):
	tei_id = str(tei_ids_list)[2:]
	tei_id = tei_id[:-2]
	media_url="/ststic/img/"+tei_id+".jpg"
	return media_url

def page_repr(page_list):
	#function to print page numbers (really just removes brackets)
	pagenumber = str(page_list)
	pagenumber = pagenumber[2:]
	pagenumber = pagenumber[:-2]
	return "Page: " +pagenumber
