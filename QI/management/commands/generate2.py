
2173
##### move file SW_GH1804.xml to static/xml
##### python manage.py generate SW_GH1804

##### Comment numbers correspond to additional explanation in the documentation


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
			#4
			file_name = 'static/xml/' + xml_file + '.xml'
			workbook = xlrd.open_workbook('static/xls/TEI people, places, orgs.xlsx')#LOCATION
			worksheet = workbook.sheet_by_name('Places')#LOCATION
			tree = etree.parse(file_name)
			root = tree.getroot() 
			#5
			#namespace - needs to be put before every element tag 
			ns = ""
			if root.tag[0] == "{":
				x = 1
				ns = root.tag[0]
			while root.tag[x-1] != "}":
				ns += root.tag[x]
				x += 1
			#6
			title = ""
			titlelist =[]
			for a in root.iter(ns + "titleStmt"):
				titlelist.append(a)
			if len(titlelist)>0:
				for x in root.iter(ns + "titleStmt"):
					for child in x:
						if child.tag == ns + "title":
							title = child.text
			title_fin = title
			if title.endswith("Version"):
				title_fin = title_fin.replace("\n","")
				title_fin = title_fin.replace("Version", "")
				title_fin = title_fin.replace("Electronic","")
				title_fin = title_fin.replace(": ", "")
				title_fin = title_fin.replace("  ","")
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
			#8			
			#Separating entries and the text of entries - making a list for both
			div_text = []
			#Getting everything as text for each div, so I can later take out tags
			divs = root.iter(ns + 'div')
			#Making a list of "div type=entry" elements.
			entries = []
			for div in divs:
				if div.get('type') == 'entry':
					entries.append(div)
					div_text = div_text + [etree.tostring(div)]
			#div_text is a list of strings, one for each div type= entry
			#9
			# Making the text nicer -- removing <> xml tags
			final_text = []
			#final_text is a list of div strings without tags
			for string in div_text:
				new = ""
				a = 0
				b=0
				while(a < len (string)):
					a_init = a
					if str(a)== "<":
						b = a 
						while (string[b] != ">" and b < len(string)):
							b = b + 1
						a = b+1
					else:
						new = new + str(a_init)
						a = a+1
				final_text = final_text + [new]
				#final_text is a list of div strings without tags
			#10
			#Getting page breaks:
			objects = [0]*len(entries)	
			#creates list of zeroes to later hold pseudo-json objects	
			pages = []
			for f,e in enumerate(entries):
				for child in e:
					page = []
					if child.tag == ns + "pb":
						page = page + [child.get("n")]
					else:
						for ch in child:
							if ch.tag == ns + "pb":
								page = page + [ch.get("n")]
							else:
								for c in ch:
									if c.tag == ns + "pb":
										page = page + [c.get("n")]		
				pages.append(page)
			####getting first possible page for overview slide
			#11
			first_page = 0
			all_pb = []
			for c in root.iter(ns + "pb"):
				all_pb.append(c.get("n"))
			#12
			fp_new = "" #new first page
			if "[" in all_pb[0] or "]" in all_pb[0]:
				for s in range(0,len(all_pb[0])):
					if all_pb[0][s] != "[" and all_pb[0][s] != "]":
						fp_new = fp_new + all_pb[0][s]	
			else:
				fp_new = all_pb[0]
			if pb_start(entries, ns) == True:
				pages_final = get_pages_alt(pages)
				first_page = int(fp_new)
			else:
				pages_final = get_pages(pages)
				first_page = int(fp_new) - 1
			#13
			###OBJECTS DEFINED HERE - Getting date and location data
			for f,e in enumerate(entries): 
			#f is int, e are "div type=entry" elements
				for child in e:
					if child.tag == ns + "dateline":
						dateline = child
						for child in dateline:
							if child.tag == ns +"placeName":
								place = child.get("key")
							if child.tag == ns+"date":
								date = child.get("when")
				'''
				teiId = place #LOCATION
				print place, "Place"
				found = False#LOCATION
				row = 0#LOCATION

				while (worksheet.cell(row, 0).value != xlrd.empty_cell.value and found == False):#LOCATION
					#print worksheet.cell(row, 0).value, "value"
					if worksheet.cell(row, 0).value == teiId:#LOCATION
						found = True#LOCATION
					else:#LOCATION
						row +=1#LOCATION
				lat = worksheet.cell(row, 4).value#LOCATION
				lon = worksheet.cell(row, 5).value#LOCATION
				'''
				#print place
				
				dj_place_list = Place.objects.filter(id_tei=place)
				print (dj_place_list)
				dj_place="Blue"
				if dj_place_list==None or dj_place_list==list() or len(dj_place_list)==0: #This stopped working overnight. Just want to know if query was unsuccessful				
					print (place, "not found in database \n")
					continue
				else:
					for i in dj_place_list:
						if i.latitude != None:
							dj_place = i
							break
						else:
							dj_place = i
						print ("DID THIS")
				lat = dj_place.latitude
				lon = dj_place.longitude
				#filler latitude/longitude
				if lat == '':#LOCATION
					print ("No lat long for",place,"I set this to lat to 42 and lon to 83. \n")
					lat = 42 #LOCATION
				if lon == '':#LOCATION
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
				objects[f] = {"location":{"lat" : float(lat), "lon": -float(lon)}, "text":{"headline": date_repr(date), "text" : final_text[f]}, "media":{"url":  media_url_repr(xml_file,pages_final[f]), "caption" : page_repr(pages_final[f])} }
			#14
			#ADDING OVERVIEW INFORMATION
			overview_media_url="/static/img/"+xml_file+"_001"+".jpg"
			final = [{"type": "overview", "text":{"headline": title_fin, "text" : description},"media":{"url": overview_media_url,  "caption" : "First Page"} }] + objects
			#Adding JSON Outside bits - 3/29/2016 
			final2 = {"calculate_zoom": False, "storymap": {"call_to_action": True, "map_type": "stamen:toner-lite", "map_as_image": False, "slides": final}}
			data = final2			#15
			with open('static/json/' + xml_file + '.json', 'w') as outfile:
				json.dump(data, outfile, sort_keys=True)
			#16	
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
	      <h2 class = "text-center" style = "font-family: 'Alegreya Sans SC'; font-weight: 400; color: white"> StoryMap for """+ xml_file + """</h2>
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
			html_file = open('templates/story_maps/' +xml_file + '.html', 'w')
			html_file.write(html_str)
			html_file.close() #creates html template
			#17
			#adds to list of xml ids to be made into urls
			file_names = 'static/xml/xml_file_names.xml'
			tree = etree.parse(file_names)
			root = tree.getroot()
			list_of_files = []
			for child in root:
				list_of_files.append(child.text)

			new_file = False #Use this existing code to detirmine if I need to add a new file to storymapdir
			if xml_file not in list_of_files:
				x = etree.SubElement(root, 'file')
				x.text = xml_file
				tree.write('static/xml/xml_file_names.xml')
				new_file = True
			new_file = True #delete this when ready, just for testing
			if new_file:
				mynewfile=""
				with open('templates/list_of_storymaps.html', 'r+') as f:
					html_as_string=f.read()
					print (html_as_string)
					soup = BeautifulSoup(html_as_string, 'html.parser')
					sml = soup.find(id='storymaplist')
					links = soup.find_all('a')
					newtag= soup.new_tag('a', id='SMLink', href=xml_file)
					atag= soup.new_tag('a', href=xml_file)
					imgtag= soup.new_tag('img', src='../static/img/'+xml_file+'_001.jpg')
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



					
					#soup.ul.append(newtag)
					#newtag.string= title_fin
					#newtag.append(imgtag)
					#newtag.wrap(soup.new_tag('li', id='SMListitem'))
					#print soup
					mynewfile = soup.prettify()
				with open('templates/list_of_storymaps.html', 'w') as f:	
					f.write(mynewfile)
			
def pb_start(entries, ns):
	#determines whether a document has page breaks at the ends of entries or the 
	#beginning of entries when an entry starts on a new page
	#returns True if an element starts with a page break
	for x in entries:
		children = []
		for child in x:
			children.append(child)
		if children[0].tag == ns +"pb":
			return True
	return False#18

def page_repr(page_list):
	#function to print page numbers (really just removes brackets)
	page_string = str(page_list)
	new = ""
	for s in range(0,len(page_string)):
		if page_string[s] != "[" and page_string[s] != "]":
			new = new + page_string[s]
	if len(page_list)== 1:
		return "Page: " +new
	else:	
		return "Pages: "+new#19
		
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
	
def get_pages(page_list_a):
		#shifting list of page breaks back one so it will be the list of page numbers
	page_list_b = page_list_a #list of lists
	#subtracts one from each page break associated with each div
	for p in range(0, len(page_list_a)):
		if page_list_a[p]!= []:
			for x in range(0,len(page_list_a[p])):
				page_list_b[p][x] = int(page_list_a[p][x]) - 1

	#only deals with the beginning part
	fill = [0]
	if page_list_a[0] == []:
		x = 0
		while x < len(page_list_a) and page_list_a[x] == []:
			x+=1
		if x < len(page_list_a):
			fill = [int(page_list_a[x][0])]
		
		for y in range(0,x):
			page_list_b[y] = fill
	else:
		fill = page_list_a[0]
		
	#now need to do rest
	
	for n in range(0, len(page_list_a)):
		if page_list_a[n] == []:
			page_list_b[n].append(fill[0]+1)
		else:
			if len(page_list_a[n]) == 1:
				fill = page_list_a[n]
			else:
				fill = [page_list_a[n][len(page_list_a[n])-1]]
	return page_list_b#21
	
def get_pages_alt(page_list_a):
	#get pages alternate is designed for refining the list of pages in
	#cases where a page break might be at the beginning of an entry but we're not sure
	#I am probably going to just not shift the numbers back
	page_list_b = page_list_a #list of lists
	for p in range(0, len(page_list_a)):
		if page_list_a[p]!= []:
			for x in range(0,len(page_list_a[p])):
				page_list_b[p][x]= int(page_list_a[p][x]) #same except no minus 1
				
		#only deals with the beginning part
	fill = [0]
	if page_list_a[0] == []:
		x = 0
		while x < len(page_list_a) and page_list_a[x] == []:
			x+=1
		if x < len(page_list_a):
			fill = [int(page_list_a[x][0])]
		
		for y in range(0,x):
			page_list_b[y] = fill
	else:
		fill = page_list_a[0]
	
	#now need to do rest
	for n in range(0, len(page_list_a)):
		if page_list_a[n] == []:
			page_list_b[n].append(int(fill[0])+1)
		else:
			if len(page_list_a[n]) == 1:
				fill = page_list_a[n]
			else:
				fill = [page_list_a[n][len(page_list_a[n])-1]]
	return page_list_b#22

def media_url_repr(file_name,page_list):
	media_url=""
	if len(page_list)==1:
		index = str(page_list[0]) #get the corresponded page number in manuscript 
		if len(index) == 1:
			index =  "_00" + index  #for example, page 2, want 002
		elif len(index) == 2:
			index = "_0"  + index
		else:
			index="_"+index 
			#for example, page 11,344 want 011, 344                elif len(index)==2:
		media_url=media_url+"/static/img/"+ file_name+index+".jpg" 
		return media_url
	else: #cases when, for example Pages:24,25 
		for i in range(0,len(page_list)):
			index = str(page_list[i]) 
			if len(index) == 1:
				index =  "00" + index  #for example, page 2, want 002
			elif len(index) == 2:
                	        index = "_0"  + index
			else:
				index="_"+index
			#for example, page 11,344 want 011, 344
			media_url=media_url+"/static/img/"+ file_name+index+".jpg"  
		return media_url   
