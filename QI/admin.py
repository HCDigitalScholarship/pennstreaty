from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources 
from QI.models import Person, Place, Organization, RoleType
from django.forms import *
from django.db import models

class PersonResource(resources.ModelResource):
	class Meta:
		model = Person
		fields = ('id', 'id_tei', 'uri_lcnaf', 'last_name', 'first_name', 'middle_name', 'other_names', 'birth_date', 'death_date', 'birth_place', 'death_place', 'gender', 'role', 'role2', 'role3', 'affiliation', 'notes', 'PYM_index')

class PersonAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'uri_lcnaf', 'last_name', 'first_name', 'middle_name', 'other_names', 'birth_date', 'death_date', 'birth_place', 'death_place', 'gender', 'role', 'role2', 'role3', 'affiliation', 'notes', 'PYM_index']
	resource_class = PersonResource
	pass

############################## break between classes ##############################


class PlaceResource(resources.ModelResource):
	class Meta:
		model = Place
		fields = ('id', 'id_tei', 'name', 'state', 'latitude', 'longitude', 'notes', 'place_type', 'alternate')

class PlaceAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'name', 'state', 'latitude', 'longitude', 'notes', 'place_type', 'alternate']
	resource_class = PlaceResource
	pass

############################## break between classes ##############################


class OrganizationResource(resources.ModelResource):
	class Meta:
		model = Organization
		fields = ('id', 'id_tei', 'organization_name', 'notes', 'associated_spellings', 'PYM_index')

class OrganizationAdmin(ImportExportModelAdmin):
	fields = ['id_tei', 'organization_name', 'notes', 'associated_spellings', 'PYM_index']
	resource_class = OrganizationResource
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



admin.site.register(Person,PersonAdmin)
admin.site.register(Place,PlaceAdmin)
admin.site.register(Organization,OrganizationAdmin)
admin.site.register(RoleType,RoleTypeAdmin)