import xml.etree.ElementTree as ET
import os
import re
import csv
from lxml import etree
import lxml.etree as ET
from html5lib.sanitizer import HTMLSanitizerMixin
from bs4 import BeautifulSoup
from QI.models import Manuscript,Page
from HTMLParser import HTMLParser
from html import HTML

def xml_to_html(xml_file):
  django_tag_open = []
  page_html = HTML()
  class MyHTMLPaser(HTMLParser):
    def handle_starttag(self,tag,attrs):
      if tag == "persName":
        django_tag_open.append("persName")
        page_html.a( 
        #would need to know stuff, maybe can still make work, but ehhh

