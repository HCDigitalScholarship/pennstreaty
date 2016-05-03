from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget
from QI.models import Person, Place, Organization, RoleType, Relationship, RelationshipType, Location, LocType, Org, Affiliation, Manuscript, Page, Book, Author
from django.forms import *
from django.db import models

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
		    if field_name=='author':#Right now this is being hard coded, but I might be able to right something that would check what types of fields there were and do this for the foreign keys
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
					print "Ooo we match a ticha id, we need to do something"
					data[field_name]= i.id
										
					print new_data[index], "#####"
				index = index + 1 	
			if not match:
				print "No matching ticha id for:",data[field_name],",:("
		
			#continue
		    print obj, "Obj"
		    print  data, "data"
		    self.import_field(field, obj, data)
		'''
		for field in self.get_fields():
		    data=Person.objects.all()
		    for i in data:
			if obj==i:
				pass
		    self.import_field(field, obj, data)
		'''

	#Aight, this is now working. Fields seemings just does not work the way it is supposed to. But I may have FINALLY FOUND THE SOLUTION TO THE INMPORTING FOREIGN KEYS PROBLEM
#I don't think this actually worked
	author = fields.Field(
	widget=ForeignKeyWidget(Person, 'first_name'))
	class Meta:
		model = Book
		fields = ('id','name','author')
class BookAdmin(ImportExportModelAdmin):
	fields = ['id','name','author']
	resource_class=BookResource
	list_display = ('id','name','author')


class PersonResource(resources.ModelResource):
#Not sure if I need to change these as well as the admin fields
#this is what changes what gets imported
	#pass
	#birth_place = fields.Field(widget=widgets.ForeignKeyWidget(Place,'name'))	
	class Meta:
		model = Person
		#birth_place = fields.Field(widget=widgets.ForeignKeyWidget(Place,'name'))	
		#95% sure this is uneccessary, pretty sure this is just white listing fields, but if we want them all, typing all this was dumb
		fields =('id', 'id_tei', 'uri_lcnaf', 'last_name', 'first_name', 'middle_name','display_name', 'other_names', 'birth_date', 'death_date', 'birth_place', 'death_place', 'gender', 'affiliation1', 'affiliation2', 'bio_notes', 'data_notes','citations', 'notes', 'PYM_index','affiliations')
		#exclude = ('id')
class PersonAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'uri_lcnaf', 'last_name', 'first_name', 'middle_name','display_name', 'other_names', 'birth_date', 'death_date', 'birth_place', 'death_place', 'gender', 'affiliation1', 'affiliation2', 'bio_notes', 'data_notes','citations', 'notes', 'PYM_index','affiliations']
	resource_class = PersonResource
	list_display = ('last_name' , 'first_name', 'id_tei')
	pass

############################## break between classes ##############################

#Changed in g doc to match, may want to change back at some point. originals can be found next to their names in models

class PlaceResource(resources.ModelResource):
	class Meta:
		model = Place
		fields = ('id', 'id_tei', 'name', 'county','state', 'latitude', 'longitude', 'notes', 'Type', 'Alternate', 'Date')

class PlaceAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'name', 'state', 'latitude', 'longitude', 'notes', 'notes2', 'place_type', 'alternate']
	resource_class = PlaceResource
	list_display = ('name', 'id_tei')
	pass

############################## break between classes ##############################


class OrganizationResource(resources.ModelResource):
	class Meta:
		model = Organization
		fields = ('id', 'id_tei', 'organization_name', 'notes', 'associated_spellings', 'PYM_index')

class OrganizationAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'organization_name', 'notes', 'associated_spellings', 'PYM_index']
	resource_class = OrganizationResource
	#THIS IS THE SOLUTION TO LISTING THE THINGS
	list_display = ('organization_name','id_tei')
	pass

############################## break between classes ##############################


class RoleTypeResource(resources.ModelResource):
	class Meta:
		model = RoleType
		fields = ('id', 'role', 'description')

class RoleTypeAdmin(ImportExportModelAdmin):
	fields = ['role', 'description']
	resource_class = RoleTypeResource
	pass

############################## break between classes ##############################

class RelationshipResource(resources.ModelResource):
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
	class Meta:
		model = Org
		fields = ['id','id_tei','name', 'place_id']
class OrgAdmin(ImportExportModelAdmin):
	fields = ['id_tei','name', 'place_id']
	resource_class = OrgResource
	list_display=(['name'])

############################## break between classes ##############################

class AffiliationResource(resources.ModelResource):
	class Meta:
		model = Org
		fields = ['id','id_tei','person_id', 'org_id']
class AffiliationAdmin(ImportExportModelAdmin):
	fields = ['id_tei','person_id', 'org_id']
	resource_class = AffiliationResource

############################## break between classes ##############################

class ManuscriptResource(resources.ModelResource):
	class Meta:
		model = Manuscript
		fields = ['id', 'id_tei', 'title', 'person_id', 'date', 'type_of_Manuscript', 'call_no']
class ManuscriptAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'title', 'person_id', 'date', 'type_of_Manuscript', 'call_no']
	resource_class = ManuscriptResource

############################## break between classes ##############################

class PageResource(resources.ModelResource):
	class Meta:
		model = Page
		fields = ['id', 'id_tei', 'Manuscript_id', 'img_url', 'fulltext']
class PageAdmin(ImportExportModelAdmin):
	class Meta:
		fields = ['id_tei', 'Manuscript_id', 'img_url', 'fulltext']
		resource_class = PageResource

#admin.site.register(Person,PersonAdmin)
admin.site.register(Person)
#admin.site.register(Place,PlaceAdmin)
admin.site.register(Place)
#admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Organization)
#admin.site.register(RoleType,RoleTypeAdmin)
admin.site.register(RoleType)

#admin.site.register(Relationship,RelationshipAdmin)
admin.site.register(Relationship)
#admin.site.register(RelationshipType,RelationshipTypeAdmin)
admin.site.register(RelationshipType)
#admin.site.register(Location,LocationAdmin)
admin.site.register(Location) #changed - not sure why but it works
#admin.site.register(LocType,LocTypeAdmin)
admin.site.register(LocType)#changed

#admin.site.register(Org,OrgAdmin)
admin.site.register(Org)
#admin.site.register(Affiliation,AffiliationAdmin)
admin.site.register(Affiliation)
#admin.site.register(Manuscript,ManuscriptAdmin)
admin.site.register(Manuscript)
#admin.site.register(Page,PageAdmin)
admin.site.register(Page)
#admin.site.register(Book,BookAdmin)
admin.site.register(Book)


