from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget
from QI.models import Person, Place, RoleType, Relationship, RelationshipType, Location, LocType, Org, Affiliation, Manuscript, Page
from django.forms import *
from django.db import models

#This is an example work thru I made
'''
#Nearly done this I think, stil trying to right it more generally, but I could just hard code them all it is not that big of a deal
class BookResource(resources.ModelResource):
	def import_obj(self, obj, data, dry_run):
		print obj, "OBJ"
		#print field.field.widget.input_type
		#self.get_fields()[0].db_type()
		for field in self.get_fields():
		    print field,"field"
		    print self.get_field_name(field)
		    field_name=self.get_field_name(field)
		    if field_name=='author':#I might be able to right something that would check what types of fields there were and do this for the foreign keys
			new_data=Person.objects.all()
			print new_data
			print data[field_name], "data fieldname"
			match=False
			index = 0
			for i in new_data:
				#print i.first_name 
				#print Person.objects.i
				
				#if i wanted to do this for a diliniated list, I would just separate out the list, and then check to see if each of them match any of the tei ids 
				if str(i) == str(data[field_name]):
					match=True
					print 
					print "Ooo we match a TEI id, we need to do something"
					data[field_name]= i.id
										
					print new_data[index], "#####"
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
		
			#continue
		    print obj, "Obj"
		    print  data, "data"
		    self.import_field(field, obj, data)
'''
'''
		for field in self.get_fields():
		    data=Person.objects.all()
		    for i in data:
			if obj==i:
				pass
		    self.import_field(field, obj, data)
'''
'''
	#Aight, this is now working. Fields seemings just does not work the way it is supposed to. But I may have FINALLY FOUND THE SOLUTION TO THE INMPORTING FOREIGN KEYS PROBLEM
#I don't think this actually worked
	#author = fields.Field(
	#widget=ForeignKeyWidget(Person, 'first_name'))
	class Meta:
		model = Book
		fields = ('id','name','author')
class BookAdmin(ImportExportModelAdmin):
	fields = ['name','author']
	resource_class=BookResource
	list_display = ('id','name','author')
'''

class PersonResource(resources.ModelResource):
	#redefining import obj so that it switches the tei ids for foreign keys and many-to-many cases into ids
	#there is almost definitely a better (built-in) way to do this...
	#But this works...
	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)
		    if (field_name=='birth_place' and 'birth_place' in data) or (field_name=='death_place' and 'death_place' in data):
			
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
				print "This is related to",field_name,'for person:',data['id_tei'],"\n"
				continue
	  	    elif field_name=='affiliations' and 'affiliations' in data:
			new_data=Org.objects.all()
			match=False
			index = 0
			mylist=[]
			mystr=""
			if data[field_name]=='review' or data[field_name]=='Review':
				data[field_name]=None
				continue
			for item in str(data[field_name]):
				if item <> ";":
					mystr=mystr+item
				else:
					mylist=mylist+[mystr.lower()]
					mystr=""
			mylist=mylist+[mystr.lower()]
			for i in new_data:
				if str(i.id_tei) in mylist:
					match=True
					newlist= newlist + [i.id]				
					del mylist[mylist.index(str(i.id_tei))]	
				index = index + 1 	
			if mylist <> list():
				print 'Did not find a match for some affiliations:',mylist
				print "This is for", data['id_tei'],"\n"
			if not match:
				print "NO matching TEI id for:",data[field_name]," in many-to-many import",mylist
				print 'This item will have NO affiliations'
				print "This is for", data['id_tei'],'\n\n'
				
				data[field_name]=None
				continue
		    if field_name<>'affiliations':
		    	self.import_field(field, obj, data)
		    else:
			data['affiliations']=str(newlist)[1:-1]

	
	class Meta:
		model = Person
		#birth_place = fields.Field(widget=widgets.ForeignKeyWidget(Place,'name'))	
		#95% sure this is uneccessary, pretty sure this is just white listing fields, but if we want them all, typing all this was dumb
		fields =('id', 'id_tei', 'lcnaf_uri', 'last_name', 'first_name', 'middle_name','display_name', 'other_names', 'birth_date', 'death_date', 'birth_place', 'death_place', 'gender', 'affiliation1', 'affiliation2', 'bio_notes', 'data_notes','citations', 'notes', 'PYM_index','affiliations')
		#exclude = ('id')
class PersonAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'lcnaf_uri', 'last_name', 'first_name', 'middle_name','display_name', 'other_names', 'birth_date', 'death_date', 'birth_place', 'death_place', 'gender','bio_notes', 'data_notes','citations', 'notes', 'PYM_index','affiliations']
	resource_class = PersonResource
	def the_affiliations(self,obj):	
		print obj.affiliations, "aff"
		aff_list = obj.affiliations.all()
		mystring=""
		for aff in aff_list:
			mystring = mystring+aff.organization_name+", "
		#check if 1 otherwise this
		if mystring==", ":
			return "(none)"
		else:
			return mystring[0:-2]
	search_fields=(['id_tei','last_name','first_name','affiliations__id_tei','affiliations__organization_name',])
	list_display = ('last_name' , 'first_name', 'id_tei','the_affiliations')
	pass

############################## break between classes ##############################

#Changed in g doc to match, may want to change back at some point. originals can be found next to their names in models

class PlaceResource(resources.ModelResource):

		
	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)

		    if (field_name=='location_id' and 'location_id' in data):
			
			
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
				continue

		    self.import_field(field, obj, data)






	class Meta:
		model = Place
		#fields = ('id', 'id_tei', 'name', 'county','state','Latitude (N)', 'Longitude (W)', 'Notes', 'Type', 'Alternate', 'Date')

class PlaceAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'name', 'state', 'latitude', 'longitude', 'notes', 'notes2', 'place_type', 'alternate','date']
	resource_class = PlaceResource
	list_filter = ("state",)
	search_fields=(['id_tei', 'name', 'state'])
	list_display = ('id_tei','name','state')
	pass

############################## break between classes ##############################
#This one is dead
'''

class OrganizationResource(resources.ModelResource):
#this class might be dead, I made a new org. Or I need to combine them? To be determined

	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)
		    if (field_name=='place_id ' and 'place_id' in data):	
			
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
		
		    self.import_field(field, obj, data)


	class Meta:
		model = Organization
		fields = ('id', 'id_tei', 'organization_name', 'notes', 'associated_spellings', 'PYM_index','place_id')

class OrganizationAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'organization_name', 'notes', 'associated_spellings', 'PYM_index','place_id']
	resource_class = OrganizationResource
	#THIS IS THE SOLUTION TO LISTING THE THINGS
	list_display = ('organization_name','id_tei')
	pass
'''
############################## break between classes ##############################

#This one might be dead as well
class RoleTypeResource(resources.ModelResource):
	class Meta:
		model = RoleType
		fields = ('id', 'role', 'description')

class RoleTypeAdmin(ImportExportModelAdmin):
	fields = ['role', 'description']
	search_fields=(['role'])
	resource_class = RoleTypeResource
	pass

############################## break between classes ##############################

class RelationshipResource(resources.ModelResource):


	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)
		    if (field_name=='subject_id' and 'subject_id' in data) or (field_name=='relationship_type_id' and 'relationship_type_id' in data) or (field_name=='object_id' and 'object_id' in data):
			
			
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
		    self.import_field(field, obj, data)


	class Meta:
		model = Relationship
		fields = ['id','id_tei', 'subject_id', 'relationship_type_id', 'object_id']
class RelationshipAdmin(ImportExportModelAdmin):
	fields = ['id_tei','subject_id', 'relationship_type_id', 'object_id']
	resource_class = RelationshipResource
	pass

############################## break between classes ##############################
class RelationshipTypeResource(resources.ModelResource):
	class Meta:
		model = RelationshipType
		fields = ['id','id_tei','relationship_type']
class RelationshipTypeAdmin(ImportExportModelAdmin):
	fields = ['relationship_type']
	resource_class = RelationshipTypeResource
	list_display = (['relationship_type'])
	pass

############################## break between classes ##############################

class LocationResource(resources.ModelResource):


	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)
		    if (field_name=='loc_type_id' and 'loc_type_id' in data):
					
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
		

		    self.import_field(field, obj, data)



	class Meta:
		model = Location
		fields = ['id', 'id_tei','name' , 'latitude', 'longitude', 'loc_type_id']

class LocationAdmin(ImportExportModelAdmin):
	fields = ['id_tei','name' , 'latitude', 'longitude', 'loc_type_id']
	resource_class = LocationResource
	list_display = (['name'])

############################## break between classes ##############################

class LocTypeResource(resources.ModelResource):
	class Meta:
		model = LocType
		fields = ['id','id_tei','loc_type'] 
class LocTypeAdmin(ImportExportModelAdmin):
	fields = ['id_tei','loc_type']
	resource_class = LocTypeResource
	list_display = (['loc_type'])

############################## break between classes ##############################

class OrgResource(resources.ModelResource):


	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)
		    if (field_name=='place_id ' and 'place_id' in data):	
			
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
				continue
		    self.import_field(field, obj, data)

	class Meta:
		model = Org
		fields = ('id', 'id_tei', 'organization_name',  'associated_spellings', 'PYM_index','place_id','other_names','date_founded','date_dissolved','org_type','data_notes','notes','lcnaf_uri','citations')
class OrgAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'organization_name', 'notes', 'associated_spellings', 'PYM_index','place_id','other_names','date_founded','date_dissolved','org_type','data_notes','lcnaf_uri','citations']
	resource_class = OrgResource
	list_filter = ("org_type",)
	search_fields=(['id_tei', 'organization_name'])
	list_display=(['id_tei','organization_name','org_type'])

############################## break between classes ##############################

class AffiliationResource(resources.ModelResource):


	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)
		    if (field_name=='person_id' and 'person_id' in data) or (field_name=='org_id' and 'org_id' in data):
			
			
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
		
		    self.import_field(field, obj, data)

	class Meta:
		model = Org
		fields = ['id','id_tei','person_id', 'org_id']
class AffiliationAdmin(ImportExportModelAdmin):
	fields = ['id_tei','person_id', 'org_id']
	resource_class = AffiliationResource

############################## break between classes ##############################

class ManuscriptResource(resources.ModelResource):

	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)
		    if (field_name=='person_id' and 'person_id' in data):
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
		    #Leaving this framework in for this one, it could be useful eventually 
	  	    elif field_name=='affiliations' and 'affiliations' in data:
			new_data=Org.objects.all()
			match=False
			index = 0
			mylist=[]
			mystr=""
			for item in str(data[field_name]):
				if item <> ";":
					mystr=mystr+item
				else:
					mylist=mylist+[mystr.lower()]
					mystr=""
			mylist=mylist+[mystr.lower()]
			for i in new_data:
				print i.id_tei,i.id
				if str(i.id_tei) in mylist:
					match=True
					newlist= newlist + [i.id]					
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name]," in many-to-many import,:("
		    if field_name<>'affiliations':
		    	self.import_field(field, obj, data)
		    else:
			data['affiliations']=str(newlist)[1:-1]


	class Meta:
		model = Manuscript
		fields = ['id', 'id_tei', 'title', 'person_id', 'date', 'type_of_Manuscript', 'call_no']
class ManuscriptAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'title', 'person_id', 'date', 'type_of_Manuscript', 'call_no']
	resource_class = ManuscriptResource

############################## break between classes ##############################

class PageResource(resources.ModelResource):


	def import_obj(self, obj, data, dry_run):
		newlist=[]
		for field in self.get_fields():
		    skip=False
		    field_name=self.get_field_name(field)
		    if (field_name=='Manuscript_id' and 'Manuscript_id' in data):
	
			new_data=Place.objects.all()
			match=False
			index = 0
			for i in new_data:
				if str(i.id_tei) == str(data[field_name]):
					match=True
					data[field_name]= i.id
										
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name],",:("
		
	  	    elif field_name=='affiliations' and 'affiliations' in data:
			new_data=Org.objects.all()
			match=False
			index = 0
			mylist=[]
			mystr=""
			for item in str(data[field_name]):
				if item <> ";":
					mystr=mystr+item
				else:
					mylist=mylist+[mystr.lower()]
					mystr=""
			mylist=mylist+[mystr.lower()]
			for i in new_data:
				print i.id_tei,i.id
				if str(i.id_tei) in mylist:
					match=True
					newlist= newlist + [i.id]					
				index = index + 1 	
			if not match:
				print "No matching TEI id for:",data[field_name]," in many-to-many import,:("
		    if field_name<>'affiliations':
		    	self.import_field(field, obj, data)
		    else:
			data['affiliations']=str(newlist)[1:-1]


	class Meta:
		model = Page
		fields = ['id', 'id_tei', 'Manuscript_id', 'img_url', 'fulltext']
class PageAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'Manuscript_id', 'img_url', 'fulltext']
	
	resource_class = PageResource
	search_fields = (['id_tei','Manuscript_id__title'])
	list_display = (['id_tei','Manuscript_id'])

admin.site.register(Person,PersonAdmin)
#admin.site.register(Person)
admin.site.register(Place,PlaceAdmin)
#admin.site.register(Place)
admin.site.register(RoleType,RoleTypeAdmin)
#admin.site.register(RoleType)

admin.site.register(Relationship,RelationshipAdmin)
#admin.site.register(Relationship)
admin.site.register(RelationshipType,RelationshipTypeAdmin)
#admin.site.register(RelationshipType)
admin.site.register(Location,LocationAdmin)
#admin.site.register(Location) #changed - not sure why but it works
admin.site.register(LocType,LocTypeAdmin)
#admin.site.register(LocType)#changed

admin.site.register(Org,OrgAdmin)
#admin.site.register(Org)
admin.site.register(Affiliation,AffiliationAdmin)
#admin.site.register(Affiliation)
admin.site.register(Manuscript,ManuscriptAdmin)
#admin.site.register(Manuscript)
admin.site.register(Page,PageAdmin)
#admin.site.register(Page)


