from new_XML_to_HTML import *
from django.core.management.base import BaseCommand, CommandError

#just making Tosin's code a custom admin command
class Command(BaseCommand):
	help = 'Converts XML files into good to go models and HTML'
	def add_arguments(self,parser):
		parser.add_argument('xml_file',nargs='+',type=str) #Django doc explains poorly, don't know what nargs does #Update, it is number of arguments, which really only needs to be one, + is one or more
	def handle(self, *args, **options):
		for xml in options['xml_file']:
			xml_to_html(xml) #might need to return this?
