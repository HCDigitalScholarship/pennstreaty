from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from QI.models import *
from django.forms import *
from django.db import models


class PersonResource(resources.ModelResource):
    #redefining import obj so that it switches the tei ids for foreign keys and many-to-many cases into ids
    #there is almost definitely a better (built-in) way to do this...
    #But this works...
    def import_obj(self, obj, data, dry_run):
        newlist = []
        for field in self.get_fields():
            skip = False
            field_name = self.get_field_name(field)
            if (field_name=='birth_place' and 'birth_place' in data) or (field_name=='death_place' and 'death_place' in data):
                new_data = Place.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name]= i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name],",:(")
                    print ("This is related to",field_name,'for person:',data['id_tei'],"\n")
                    continue
            elif field_name=='affiliations' and 'affiliations' in data:
                new_data = Org.objects.all()
                match = False
                index = 0
                mylist = []
                mystr = ""
                if data[field_name]=='review' or data[field_name]=='Review':
                    data[field_name] = None
                    continue
                for item in str(data[field_name]):
                    if item != ";":
                        mystr = mystr+item
                    else:
                        mylist = mylist+[mystr.lower()]
                        mystr = ""
                mylist = mylist+[mystr.lower()]
                for i in new_data:
                    if str(i.id_tei) in mylist:
                        match = True
                        newlist= newlist + [i.id]
                        del mylist[mylist.index(str(i.id_tei))]
                    index = index + 1
                if mylist != list():
                    print ('Did not find a match for some affiliations:',mylist)
                    print ("This is for", data['id_tei'],"\n")
                if not match:
                    print ("NO matching TEI id for:",data[field_name]," in many-to-many import",mylist)
                    print ('This item will have NO affiliations')
                    print ("This is for", data['id_tei'],'\n\n')
                    data[field_name] = None
                    continue
            if field_name !='affiliations':
                self.import_field(field, obj, data)
            else:
                data['affiliations'] = str(newlist)[1:-1]

    class Meta:
        model = Person
        fields = ('id', 'id_tei', 'lcnaf_uri', 'last_name', 'first_name', 'middle_name',
                  'display_name', 'other_names', 'birth_date', 'death_date', 'birth_place',
                  'death_place', 'gender', 'affiliation1', 'affiliation2', 'bio_notes',
                  'data_notes', 'citations', 'notes', 'PYM_index','affiliations')


class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource
    fields = ['id_tei', 'lcnaf_uri', 'last_name', 'first_name', 'middle_name', 'display_name',
              'other_names', 'birth_date', 'death_date', 'birth_place', 'death_place', 'gender',
              'bio_notes', 'data_notes','citations', 'notes', 'PYM_index', 'affiliations']
    filter_horizontal = ('affiliations',)
    search_fields = ['id_tei', 'last_name', 'first_name', 'affiliations__id_tei',
                     'affiliations__organization_name']
    list_display = ('last_name' , 'first_name', 'id_tei', 'the_affiliations')

    def the_affiliations(self,obj):
        aff_list = obj.affiliations.all()
        mystring = ""
        for aff in aff_list:
            mystring = mystring+aff.organization_name+", "
        #check if 1 otherwise this
        if mystring==", ":
            return "(none)"
        else:
            return mystring[0:-2]


#Changed in g doc to match, may want to change back at some point. originals can be found next to their names in models
class PlaceResource(resources.ModelResource):
    def import_obj(self, obj, data, dry_run):
        newlist = []
        for field in self.get_fields():
            skip = False
            field_name = self.get_field_name(field)
            if (field_name=='location_id' and 'location_id' in data):
                new_data = Place.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name]= i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name],",:(")
                    continue
            self.import_field(field, obj, data)

    class Meta:
        model = Place


class PlaceAdmin(ImportExportModelAdmin):
    fields = ['id_tei', 'name', 'state', 'latitude', 'longitude', 'notes', 'notes2',
              'place_type', 'alternate','date']
    resource_class = PlaceResource
    list_filter = ("state",)
    search_fields = ['id_tei', 'name', 'state']
    list_display = ('id_tei', 'name', 'state')


#This one might be dead as well
class RoleTypeResource(resources.ModelResource):
    class Meta:
        model = RoleType
        fields = ('id', 'role', 'description')


class RoleTypeAdmin(ImportExportModelAdmin):
    fields = ['role', 'description']
    search_fields = (['role'])
    resource_class = RoleTypeResource


class RelationshipResource(resources.ModelResource):
    def import_obj(self, obj, data, dry_run):
        newlist = []
        for field in self.get_fields():
            skip = False
            field_name = self.get_field_name(field)
            if (field_name=='subject_id' and 'subject_id' in data) or (field_name=='relationship_type_id' and 'relationship_type_id' in data) or (field_name=='object_id' and 'object_id' in data):
                new_data = Place.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name]= i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name],",:(")
            self.import_field(field, obj, data)

    class Meta:
        model = Relationship
        fields = ['id','id_tei', 'subject_id', 'relationship_type_id', 'object_id']


class RelationshipAdmin(ImportExportModelAdmin):
    fields = ['id_tei', 'subject_id', 'relationship_type_id', 'object_id']
    resource_class = RelationshipResource


class RelationshipTypeResource(resources.ModelResource):
    class Meta:
        model = RelationshipType
        fields = ['id', 'id_tei', 'relationship_type']


class RelationshipTypeAdmin(ImportExportModelAdmin):
    fields = ['relationship_type']
    resource_class = RelationshipTypeResource
    list_display = ['relationship_type']


class LocationResource(resources.ModelResource):
    def import_obj(self, obj, data, dry_run):
        newlist = []
        for field in self.get_fields():
            skip = False
            field_name = self.get_field_name(field)
            if (field_name=='loc_type_id' and 'loc_type_id' in data):
                new_data = Place.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name]= i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name],",:(")
            self.import_field(field, obj, data)

    class Meta:
        model = Location
        fields = ['id', 'id_tei', 'name', 'latitude', 'longitude', 'loc_type_id']


class LocationAdmin(ImportExportModelAdmin):
    fields = ['id_tei', 'name', 'latitude', 'longitude', 'loc_type_id']
    resource_class = LocationResource
    list_display = ['name']


class LocTypeResource(resources.ModelResource):
    class Meta:
        model = LocType
        fields = ['id', 'id_tei', 'loc_type']


class LocTypeAdmin(ImportExportModelAdmin):
    fields = ['id_tei', 'loc_type']
    resource_class = LocTypeResource
    list_display = ['loc_type']


class OrgResource(resources.ModelResource):
    def import_obj(self, obj, data, dry_run):
        newlist = []
        for field in self.get_fields():
            skip = False
            field_name = self.get_field_name(field)
            if (field_name=='place_id ' and 'place_id' in data):
                new_data = Place.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name]= i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name],",:(")
                    continue
            self.import_field(field, obj, data)

    class Meta:
        model = Org
        fields = ('id', 'id_tei', 'organization_name',  'associated_spellings', 'PYM_index',
                  'place_id', 'other_names', 'date_founded', 'date_dissolved', 'org_type',
                  'data_notes', 'notes', 'lcnaf_uri', 'citations')


class OrgAdmin(ImportExportModelAdmin):
    fields = ['id_tei', 'organization_name', 'notes', 'associated_spellings', 'PYM_index',
              'place_id', 'other_names', 'date_founded', 'date_dissolved', 'org_type', 'data_notes',
              'lcnaf_uri', 'citations']
    resource_class = OrgResource
    list_filter = ("org_type",)
    search_fields = (['id_tei', 'organization_name'])
    list_display = (['id_tei','organization_name','org_type'])


class AffiliationResource(resources.ModelResource):
    def import_obj(self, obj, data, dry_run):
        newlist = []
        for field in self.get_fields():
            skip = False
            field_name = self.get_field_name(field)
            if (field_name=='person_id' and 'person_id' in data) or (field_name=='org_id' and 'org_id' in data):
                new_data = Place.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name]= i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name],",:(")
            self.import_field(field, obj, data)

    class Meta:
        model = Org
        fields = ['id','id_tei','person_id', 'org_id']


class AffiliationAdmin(ImportExportModelAdmin):
    fields = ['id_tei','person_id', 'org_id']
    resource_class = AffiliationResource


class ManuscriptResource(resources.ModelResource):
    def import_obj(self, obj, data, dry_run):
        newlist = []
        for field in self.get_fields():
            skip = False
            field_name = self.get_field_name(field)
            if (field_name=='person_id' and 'person_id' in data):
                new_data = Person.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name]= i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name],",:(")
            elif (field_name=='org_id' and 'org_id' in data):
                new_data = Org.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name] = i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name])
            #Leaving this framework in for this one, it could be useful eventually
            elif field_name=='affiliations' and 'affiliations' in data:
                new_data = Org.objects.all()
                match = False
                index = 0
                mylist = []
                mystr = ""
                for item in str(data[field_name]):
                    if item != ";":
                        mystr = mystr+item
                    else:
                        mylist = mylist+[mystr.lower()]
                        mystr = ""
                mylist = mylist+[mystr.lower()]
                for i in new_data:
                    print (i.id_tei,i.id)
                    if str(i.id_tei) in mylist:
                        match = True
                        newlist= newlist + [i.id]
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name]," in many-to-many import,:(")
            if field_name != 'affiliations':
                self.import_field(field, obj, data)
            else:
                data['affiliations'] = str(newlist)[1:-1]

    class Meta:
        model = Manuscript
        fields = ['id', 'id_tei', 'title', 'person_id', 'person_name', 'org_id', 'org_name',
                  'location', 'summary', 'date', 'type_of_Manuscript', 'call_no']


class ManuscriptAdmin(ImportExportModelAdmin):
    fields = ['id_tei', 'title', 'person_id', 'person_name', 'org_id', 'org_name', 'location',
              'summary', 'date', 'type_of_Manuscript', 'call_no', 'transcribed']
    resource_class = ManuscriptResource
    list_display=['id_tei','title']

class PageResource(resources.ModelResource):
    def import_obj(self, obj, data, dry_run):
        newlist = []
        for field in self.get_fields():
            skip = False
            field_name = self.get_field_name(field)
            if (field_name=='Manuscript_id' and 'Manuscript_id' in data):
                new_data = Place.objects.all()
                match = False
                index = 0
                for i in new_data:
                    if str(i.id_tei) == str(data[field_name]):
                        match = True
                        data[field_name]= i.id
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name],",:(")
            elif field_name=='affiliations' and 'affiliations' in data:
                new_data = Org.objects.all()
                match = False
                index = 0
                mylist = []
                mystr = ""
                for item in str(data[field_name]):
                    if item != ";":
                        mystr = mystr+item
                    else:
                        mylist = mylist+[mystr.lower()]
                        mystr = ""
                mylist = mylist+[mystr.lower()]
                for i in new_data:
                    print (i.id_tei,i.id)
                    if str(i.id_tei) in mylist:
                        match = True
                        newlist= newlist + [i.id]
                    index = index + 1
                if not match:
                    print ("No matching TEI id for:",data[field_name]," in many-to-many import,:(")
            if field_name!='affiliations':
                self.import_field(field, obj, data)
            else:
                data['affiliations'] = str(newlist)[1:-1]

    class Meta:
        model = Page
        fields = ['id', 'id_tei', 'Manuscript_id', 'img_url', 'fulltext', 'transcribed']


class PageAdmin(ImportExportModelAdmin):
    fields = ('id_tei', 'Manuscript_id', 'img_url', 'fulltext', 'transcribed')
    resource_class = PageResource
    search_fields = (['id_tei','Manuscript_id__title'])
    list_display = (['id_tei','Manuscript_id'])


admin.site.register(Person,PersonAdmin)
admin.site.register(Place,PlaceAdmin)
admin.site.register(RoleType,RoleTypeAdmin)

admin.site.register(Relationship,RelationshipAdmin)
admin.site.register(RelationshipType,RelationshipTypeAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(LocType,LocTypeAdmin)

admin.site.register(Org,OrgAdmin)
admin.site.register(Affiliation,AffiliationAdmin)
admin.site.register(Manuscript,ManuscriptAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(PendingTranscription)
