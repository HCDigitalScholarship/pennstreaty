import xml.etree.ElementTree as ET
import os
import re
import csv
from lxml import etree
import lxml.etree as ET
from html5lib.sanitizer import HTMLSanitizerMixin
from bs4 import BeautifulSoup
from QI.models import Manuscript,Page

def xml_to_html(xml_file):
      #xml_file =  input( "Please insert path to XML file that you would like to convert to HTML:  ") 
      tree = etree.parse(xml_file)
      xml_string = etree.tostring(tree)


      new_xml_string = xml_string[xml_string.index("</teiHeader>")+12:]
      new_xml_string = new_xml_string.replace("</TEI>", "")

      #print new_xml_string

      root = etree.fromstring(new_xml_string)
      #print etree.tostring(root)

      for persName in root.iter("persName"):
            if  len(persName.items()) != 0:
                  persName.attrib["key"] = "#"+persName.items()[0][1]
            for key in persName.keys():
                  persName.attrib["href"] = persName.attrib.pop(key)
                  persName.attrib['class'] = persName.tag
                  persName.tag = "a"
          
      for placeName in root.iter("placeName"):
            if  len(placeName.items()) != 0:
                  placeName.attrib["key"] = "#"+placeName.items()[0][1]
            for key in placeName.keys():
                  placeName.attrib["href"] = placeName.attrib.pop(key)
            placeName.attrib['class'] = placeName.tag
            placeName.tag = "a"

      for orgName in root.iter("orgName"):
            if  len(orgName.items()) != 0:
                  orgName.attrib["key"] = "#"+orgName.items()[0][1]
            for key in orgName.keys():
                  orgName.attrib["href"] = orgName.attrib.pop(key)
            orgName.attrib['class'] = orgName.tag
            orgName.tag = "a"

      for geogName in root.iter("geogName"):
            if  len(geogName.items()) != 0:
                  geogName.attrib["key"] = "#"+geogName.items()[0][1]
            for key in geogName.keys():
                  geogName.attrib['href'] = geogName.attrib.pop(key)
            geogName.attrib['class'] = geogName.tag
            geogName.tag = "a"

      for date in root.iter("date"):
            date.tag = "a"
          
      for line_break in root.iter("lb"):
            line_break.tag = "br"
            line_break.attrib.clear()
          
      for page_break in root.iter("pb"):
            for attr in page_break.attrib:
                  if attr != 'n':
                        del page_break.attrib[attr]
          

      for title in root.iter("title"):
            title.tag = "h1"

      for row in root.iter("row"):
            row.tag = "tr"

      for cell in root.iter("cell"):
            cell.tag = "td"
            cell.attrib.clear()

            
      #print etree.tostring(root)

      list_of_xml_tags = [elem.tag for elem in root.iter() if elem is not root]

      for tag in list_of_xml_tags:
            if tag not in HTMLSanitizerMixin.acceptable_elements and tag != "body" and tag != "pb" :
                  etree.strip_tags(root, tag) #takes out tags that are not html tags from xml (changing to html) file


      
      #print etree.tostring(root)
      html_string = etree.tostring(root)

      soup = BeautifulSoup(html_string, "html.parser")

      #print(soup.prettify())

      page_break_loc = soup.find_all('pb')#collects all pb tags into a list. list is composed of pb tag with closing tag for each pb tag
      #print page_break_loc, "This is the page break locs"
      #the next two for loops is to properly format the pb takes in the page_break_loc so that it looks the same as the original pb tag in the xml page
      pb_list = []

      for x in page_break_loc:
            pb_list.append(re.sub('\</pb>$', '',str(x)))

      for pb in page_break_loc: #removes the closing tag
            pb_list.append(re.sub('\</pb>$', '',str(pb)))

      new_pb_list = []
      for ele in pb_list:#adds a backslash to the end of the string pb within the <>
            ele = ele[:-1]+"/"+ele[-1]
            new_pb_list.append(ele)

      for_csv = ''.join(html_string)
      
      with open("csv_for_"+os.path.basename(xml_file)+".csv", 'wb') as f:
            writer = csv.writer(f)
            count = 0
            csv_list =[]

            for pbs in new_pb_list:
                  pb_csv_list = []
                  pb_csv_list.append(os.path.basename(xml_file))
                  pb_csv_list.append(os.path.basename(xml_file)+"_pg_"+ str(count))
                  pb_csv_list.append(for_csv[:for_csv.find(pbs)])
                  csv_list.append(pb_csv_list)

                  count+=1
                  for_csv = for_csv[for_csv.find(pbs)+len(pbs):]

            pb_csv_list = []
            pb_csv_list.append(os.path.basename(xml_file))
            pb_csv_list.append(os.path.basename(xml_file)+"_pg_"+ str(count))
            pb_csv_list.append(for_csv[:for_csv.find(pbs)])
            csv_list.append(pb_csv_list)
            
            writer.writerows(csv_list)

      
      soup = BeautifulSoup(html_string, "html.parser")

      has_annoying_problem=False #pb splitting an <a> tag
      for a in soup.find_all('a'):
	if a.find_all('pb') <> list():
		print "DAMN IT, this has the problem"
		has_annoying_problem=True


      #a=soup.div.unwrap()
      #print a
      #return a
      #soup.body.unwrap()
      html=""
      html_list=[]
      for item in soup.find_all('div'):
	      dealwith=False
	      list_of_probtext = []
	      list_of_solutions = []
	      if has_annoying_problem:
		list_of_a=item.find_all('a')
		index = 0
		probdex=[]
		for a in list_of_a:
			if a.find_all('pb') <> list():
				probdex=probdex+[index]
			index = index + 1
		if probdex <> list():
			dealwith = True
			for problem in probdex:
				probtext=unicode(list_of_a[problem])
				list_of_probtext= list_of_probtext + [probtext]
				line = ""
				tag = ""
				getting_tag=True
				waitfor=False
				for char in probtext:
					if char== '>' and getting_tag:
						tag = tag + char
						getting_tag=False
					if found_pb and char == '/':
						waitfor=True
					if waitfor and char == '>':
						#print tag,"tag"
						line = line + char + tag
						waitfor=False
						found_pb=False
						continue
					if char == '<':
						saved = '<'
					elif saved == '<' and char == 'p':
						saved = '<p'			
					elif saved == '<p' and char == 'b':
						found_pb = True
						line = line  + '</a>' + saved + char
						saved = ""
					else:
						if getting_tag:
							tag=tag +saved+ char
						line = line +saved+ char
						saved = ""
				#print line
				list_of_solutions = list_of_solutions + [line]
						

		#print probdex, "PROBDEX"




	      #print item, "ITEM"
	      wholetext=unicode(item)
	      if has_annoying_problem and dealwith:
		#print list_of_probtext,list_of_solutions
		for problem,solution in zip(list_of_probtext,list_of_solutions):
			
			#print wholetext, "before"
			#print wholetext.find(problem)
			#print problem,solution 
			wholetext = wholetext.replace(problem,solution)
			#print wholetext, "after"
			print "We hopefully solved the problems, this message indicates that we took a lot of steps too"


	      saved = False
	      pb = False

	      found_pb=False
	      found_div=False
	      closed = 0
	      closed_div = 0
	      #print wholetext
	      for char in wholetext:
		if found_pb and closed <> 2:
			if char == '>':
				closed = closed + 1
				continue
			else:
				continue
		else:
			found_pb=False
		        closed = 0

		if found_div and closed_div <> 1:
			if char == '>':
				closed_div = closed_div + 1
				continue
			else:
				continue
		else:
			found_div=False
		        closed_div = 0

		if char == '<':
			pb=True
			saved=char
		elif saved == '<' and char == 'p':
			saved='<p'
		elif saved == '<' and char == 'd':
			saved = '<d'
		elif saved == '<' and char == '/':
			saved = '</'
		elif saved == '</' and char == 'd':
			saved = '<d'
		elif saved == '<d' and char == 'i':
			saved = '<di'
		elif saved == '<di' and char == 'v':
			found_div=True
			#print "FOUND IT"
			saved = ''
		elif saved == '<p' and char == 'b':
			#print "got it"
			found_pb=True
			html_list=html_list+[html]
			html=""
			saved = ""
		else:
			html = html + saved + char
			saved = ""
     # print html
     # print html_list
		
      """
      '''
      print "here is my soup"
      print soup.prettify()
      print soup.find_all('div')
    #  print soup.get_text()
  #    print "here is my soup"
      with open('sample.html','w') as f:
	f.write(html_string)
      print "WOOP"
      html=""
      html_list=[]
      for div in soup.find_all('div'):
	#print div.contents,"\n \n"  
	pb=False
	to_add=""
	was_a_pb=0
	for item in div.children:
		print item, "Item \n \n", 
		zname=item.name
		if zname == 'pb':
			html_list=html_list+[html]
			html=""
		elif zname == None:
			continue
		elif zname == 'p':
			
			for part in item.children:
				print part, "PART", part.name, "PART NAME \n \n"
				if part.name == 'pb':
					html_list=html_list+[html]
					html=""
				else:
					html= html + part.encode('utf-8')
	'''

	'''				val = part.string
					print val, "val"
					#if val != None and type(val) == type(u"") and val.find(u'\u2019') >= 0:
						#val = val.replace(u'\u2019', '\'')
					if val <> None:
						html=html+str(part)
					else:
						html=html+str(val)'''

					'''try:
						html = html + unicode(part)
					except UnicodeDecodeError:
						html = html + str(part)'''			
			#print html, "HTML"

			#html_list=html_list+[html]
			#html=""

		#else:
			#html=html+str(item)
		'''print char
		if was_a_pb <> 0:
			continue
		if char == '<':
			pb=True
			to_add=char
		elif char =='p' and pb:
			to_add=to_add+char
		elif char =='b' and pb:
			html_list=html_list+[html]
			to_add=to_add+char
			html=""
			was_a_pb=5
			pb=False

		else:
			if pb:
				html=html+to_add
			html=html+char
			pb=False
		'''
      """  

      #print os.path.basename(xml_file)
      trunc_filename=""
      for char in os.path.basename(xml_file):
	if char <> '.':
		trunc_filename=trunc_filename+char
	else:
		break
      index = 1
      #This will mean that manuscripts need to be uploaded first
      try:
      	id_manuscript=(Manuscript.objects.filter(id_tei=trunc_filename))[0]
      except IndexError:
	print "It looks like the id of the manuscript did not exist"
	print "this is going to be an error" #Might want to update this. It would be SICK if it would catch it and then throw something up on the page
	id_manuscript=None
      print id_manuscript, "man id"
      with open('sample.txt', "w") as f:
	      for html in html_list:
		if index<10:
			sindex='_00'+str(index)
		elif index<100:
			sindex='_0'+str(index)
		elif index<1000:
			sindex='_'+str(index)
		else:
			print "index got too high (over 999)! Naming convention off"
			sindex=str(index)
		new_page = Page(id_tei=trunc_filename+sindex,fulltext=html,Manuscript_id=id_manuscript)
		index = index+1
		#f.write(html)
		new_page.save()
      #print html_list
      q = Page(id_tei="sweetaction")
      #q.save()
	
	#print html_list
      print len(page_break_loc)
      if has_annoying_problem:
	print "Oy, this one has the worst corner case"
      return html_string
















