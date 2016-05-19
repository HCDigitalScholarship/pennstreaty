from django.conf.urls import url
from QI import views

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

###WOrk on this!!

urlpatterns = []
filename = 'static/xml/xml_file_names.xml'
tree = etree.parse(filename)
root = tree.getroot()
for child in root:
	xml_id = child.text
	urlpatterns.append(url(r'^' +xml_id+ '/$', views.storymap, {'xml_id': xml_id}))


#urlpatterns = [
#    url(r'^SW_GH1804/$', views.storymap, {'xml_id': 'SW_GH1804'}),
#    url(r'^SW_WH1793/$', views.storymap, {'xml_id': 'SW_WH1793'}),
#]
