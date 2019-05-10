import re
import os 
from lxml import etree
from bs4 import BeautifulSoup
import csv


##xml_file = input( "Please insert path to HTML file with XML extension:")
##html_file = input("Please insert path to same file with a HTML extension:")

def csv_page_break(xml_file,html_file):
     #I made these inputs to add it as a django admin command -Dylan 
     #xml_file = input( "Please insert path to XML file:")
     #html_file = input("Please insert path to same file with a html extension:") #need the xml file saved as a html file because of beautiful soup

      soup = BeautifulSoup(open(html_file, 'rb'), "html.parser")
      page_break_loc = soup.find_all('pb') #collects all pb tags into a list. list is composed of pb tag with closing tag for each pb tag

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
      #print new_pb_list
      #tree = etree.parse(open('/Users/oluwatosinalliyu/Desktop/forpage_break.xml'))
      #changing the xml file to a string so that it can be easily parsed through 
      tree = etree.parse(open(xml_file))
      xml_string = etree.tostring(tree)
      


      with open("csv_for_"+os.path.basename(xml_file)+".csv", 'wb') as f:
            writer = csv.writer(f)
            count = 0
            csv_list =[]
            
            for pbs in new_pb_list:
                  pb_csv_list = []
                  pb_csv_list.append(os.path.basename(xml_file))
                  pb_csv_list.append(os.path.basename(xml_file)+"_pg_"+ str(count))
                  pb_csv_list.append(xml_string[:xml_string.find(pbs)])
                  csv_list.append(pb_csv_list)
                  
                  count+=1
                  xml_string = xml_string[xml_string.find(pbs)+len(pbs):]
            #print xml_string


            pb_csv_list = []
            pb_csv_list.append(os.path.basename(xml_file))
            pb_csv_list.append(os.path.basename(xml_file)+"_pg_"+ str(count))
	    #should this stuff be in the for loop? -Dylan
            pb_csv_list.append(xml_string[:xml_string.find(pbs)])
            csv_list.append(pb_csv_list)
            
            writer.writerows(csv_list)

'''
if re.search(r' n="(\d+)"', pbs) != None:
                  pb_csv_list.append(os.path.basename(xml_file)+str(re.search(r' n="(\d+)"', pbs).group(1)))
            else:
                  pb_csv_list.append(os.path.basename(xml_file)+ str(count))

'''
           
      
