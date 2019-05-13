from page_break_csv import *
from django.core.management.base import BaseCommand, CommandError
#just making Tosin's code a custom admin command
class Command(BaseCommand):
	help = 'Does ? take xml file path and html file path'
	def add_arguments(self,parser):
		parser.add_argument('xml_file_path',nargs='+',type=str) #Django doc explains poorly, don't know what nargs does #Update, it is number of arguments, which really only needs to be one, + is one or more
		parser.add_argument('html_file_path',nargs='+',type=str) 
	def handle(self, *args, **options):
		for xml,html in zip(options['xml_file_path'],options['html_file_path']):
			csv_page_break(xml,html) #might need to return this?
