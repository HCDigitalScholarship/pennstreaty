from django.conf.urls import url
from QI import views
import xml.etree.ElementTree as etree


urlpatterns = []
filename = 'static/xml/xml_file_names.xml'
tree = etree.parse(filename)
root = tree.getroot()
for child in root:
    xml_id = child.text
    urlpatterns.append(url(r'^' +xml_id+ '/$', views.storymap, {'xml_id': xml_id}))
