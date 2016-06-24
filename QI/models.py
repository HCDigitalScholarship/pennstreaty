from django.db import models

#Note, if you can't import something, and are getting "Column 'id' not found in dataset" django really likes when you have an empty id column first. In fact, it likes it so much, it doesn't work without it.


#import a list delimited by semicolons
#Might be able to change what django/MySql uses for id field
#https://django-import-export.readthedocs.org/en/latest/getting_started.html



class Person(models.Model):

	review_status = models.CharField("TEI ID", max_length = 50)
	id_tei = models.CharField("TEI ID", max_length = 50)
	lcnaf_uri = models.CharField("URI LCNAF", max_length = 50, blank = True)
	last_name = models.CharField("Last Name", max_length=100, blank = True)
	first_name = models.CharField("First Name", max_length=100, blank = True)
	middle_name = models.CharField("Middle Name", blank = True, max_length=100)
	display_name = models.CharField("Display Name", blank = True, max_length=100)
	other_names= models.TextField("Other Names", blank = True)
	birth_date = models.CharField("Birth Date", max_length=20, blank = True)
	death_date =  models.CharField("Death Date", max_length=20, blank = True)
	birth_place = models.ForeignKey("Place", blank = True, null = True, related_name = "birthplace")
	death_place = models.ForeignKey("Place", blank = True, null = True, related_name = "deathplace")
	gender =  models.CharField("Gender", blank = True, max_length=20)
	role = models.ForeignKey("RoleType", blank =True, null=True, related_name = '%(class)s_Role_1')
	role2 = models.ForeignKey("RoleType", blank = True, null= True, related_name = '%(class)s_Role_2')
	role3 = models.ForeignKey("RoleType", blank = True, null=True, related_name = '%(class)s_Role_3')
	affiliation1 =  models.CharField("Affiliation 1", blank = True, max_length=45) #do we want a model for affiliaiton?
	affiliation2 =  models.CharField("Affiliation 2", blank = True, max_length=45)
	notes = models.TextField("Note Field", blank = True)
	bio_notes = models.TextField("Biography Note Field", blank = True)
	data_notes = models.TextField("Data Note Field", blank = True)
	citations = models.TextField("Citations", blank = True)
	PYM_index = models.TextField("PYM Index", blank = True)
	affiliations = models.ManyToManyField('Org', blank = True)
	def get_type(self):
		return 'Person'
	def __unicode__(self):
		return self.id_tei + " " + self.first_name+ " " + self.last_name # + " " + self.uri_lcnaf + " " + self.last_name + " " + self.first_name  + " " + self.middle_name + " " + self.display_name + " " + self.other_names + " " + unicode(self.birth_date) +  " " + unicode(self.death_date) + " " + unicode(self.birth_place.name) + " " + unicode(self.death_place) + " " + self.gender + " " + unicode(self.role) + " " + unicode(self.role2) + " " + unicode(self.role3) + " " + self.affiliation1 + " " + self.affiliation2 + " " + self.notes + " " + self.bio_notes + " " + self.data_notes + " " + self.citations + " "  + unicode(self.PYM_index)
#
class Place(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	name = models.CharField("Name of Place", max_length = 200, blank = True)
	county = models.CharField("County", max_length = 100, blank = True)
	state = models.CharField("State", max_length = 20, blank = True)
	latitude = models.CharField("Latitude", max_length = 15, blank = True, null = True)
	longitude = models.CharField("Longitude", max_length = 15, blank = True, null = True)
	notes = models.TextField("Description Field", blank = True)
	notes2 = models.TextField("Description Field", blank = True)
	PLACENAME = 'placeName'
	GEOGNAME = 'geogName'
	PLACE_TYPE_CHOICES = (
			(PLACENAME, 'Place Name'),
			(GEOGNAME, 'Geography Name'),
	)
   	place_type = models.CharField("Place Type", max_length=30, choices=PLACE_TYPE_CHOICES, default=PLACENAME, blank = True)
	alternate = models.TextField("Alternate Names", blank = True)

	#Some of the above will certainly get deleted, but for now, I just add
	location_id = models.ForeignKey("Location", blank = True, null=True, related_name = 'Location')
	date = models.CharField("Date", max_length = 20, blank = True)
	def get_type(self):
		return 'Place'
	def __unicode__(self):
		return self.id_tei + " " + self.name + " " + self.state + " " + unicode(self.latitude) + " " + unicode(self.longitude) + " " + self.notes + " " + self.notes2 + " "  + unicode(self.place_type) + " " + self.alternate
"""
#RIP Organization, long live org!
class Organization(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	organization_name = models.CharField("Name of Organization", max_length = 100, blank = True)
	'''
	notes = models.TextField("Note Field", blank = True)
	associated_spellings = models.TextField("Associated Spellings/Names", blank = True)
	PYM_index = models.TextField("PYM Index", blank = True)
	place_id =  models.ForeignKey("Place", blank = True, null = True, related_name = "place_id2")
	other_names =  models.CharField("Other Names of Organization", max_length = 200, blank = True)
	date_founded = models.CharField("Date Founded", max_length = 20, blank = True)
	date_dissolved = models.CharField("Date Founded", max_length = 20, blank = True)

	#####################################################
	#might need an associated places here
	#####################################################

	org_type = models.CharField("Oraganization Type", max_length = 70, blank = True)
	bio_notes = models.TextField("Description Field", blank = True)
	data_notes = models.CharField("LCNAF URI", max_length = 50, blank = True)
	notes = models.CharField("Notes", max_length = 50, blank = True)
	lcnaf_uri = models.CharField("LCNAF URI", max_length = 50, blank = True)
	citations = models.TextField("Description Field", blank = True)
	def __unicode__(self):
		return self.id_tei + " " + self.organization_name + " " + self.notes + " " + self.associated_spellings + " " + self.PYM_index
"""
## Some dumb-dumb may have accidentally put in Org when Organization already exsisted, but I am not sure what from Organization we want to keep though
class Org(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50) #all the others have this but it might be unneccessary
	organization_name = models.CharField("Name of Organization", max_length = 200, blank = True)
	place_id =  models.ForeignKey("Place", blank = True, null = True, related_name = "place_id")
	notes = models.TextField("Note Field", blank = True)
	associated_spellings = models.TextField("Associated Spellings/Names", blank = True)
	PYM_index = models.TextField("PYM Index", blank = True)
	other_names =  models.CharField("Other Names of Organization", max_length = 200, blank = True)
	date_founded = models.CharField("Date Founded", max_length = 20, blank = True)
	date_dissolved = models.CharField("Date Founded", max_length = 20, blank = True)

	#####################################################
	#might need an associated places here
	#####################################################

	org_type = models.CharField("Oraganization Type", max_length = 70, blank = True)
	bio_notes = models.TextField("Description Field", blank = True)
	data_notes = models.CharField("LCNAF URI", max_length = 50, blank = True)
	notes = models.CharField("Notes", max_length = 50, blank = True)
	lcnaf_uri = models.CharField("LCNAF URI", max_length = 50, blank = True)
	citations = models.TextField("Description Field", blank = True)
	def __unicode__(self):
		return self.id_tei + " " + self.organization_name + " " + self.notes + " " + self.associated_spellings + " " + self.PYM_index
	def get_type(self):
		return 'Group'

class RoleType(models.Model):
	role = models.CharField("Role_Type", max_length = 50, blank = True)
	description = models.TextField("Description of Role", blank = True)

	class Meta:
       		verbose_name_plural = "Role Types"

	def __unicode__(self):
		return self.role + " " + self.description

#####NEW STUFF#####


#Models describing relationship e.g. Dave | is the father of | Dylan
class Relationship(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50) #all the others have this but it might be unneccessary
	subject_id = models.ForeignKey("Person", blank = True, null = True, related_name = "subjectid")#might want to change the related names and defaults
	relationship_type_id = models.ForeignKey("RelationshipType", blank = True, null = True, related_name = "relationshipType")
	object_id = models.ForeignKey("Person", blank = True, null = True, related_name = "objectid")

	def __unicode__(self):
		return unicode(self.subject_id) + " " + unicode(self.relationship_type_id
)+ " " + unicode(self.object_id)


class RelationshipType(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50) #all the others have this but it might be unneccessary
	relationship_type = models.CharField("Relationship Type", max_length=100, blank = True)
	def __unicode__(self):
		return self.relationship_type

class Location(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	name = models.CharField("Name of Place", max_length = 200, blank = True)
	#Just followed example from old place lat/long, but this could also be ints or floats or something like that if desired
	latitude = models.CharField("Latitude", max_length = 15, blank = True, null = True)
	longitude = models.CharField("Longitude", max_length = 15, blank = True, null = True)
	loc_type_id = models.ForeignKey("LocType", blank = True, null = True, related_name = "LocationType")
	def __unicode__(self):
		return self.name

class LocType(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	loc_type = models.CharField("Name of Place", max_length = 200, blank = True)
	def __unicode__(self):
		return self.loc_type

#I think this one is unnecessary
class Affiliation(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	person_id =  models.ForeignKey("Person", blank = True, null = True, related_name = "person_id")
	org_id =  models.ForeignKey("Org", blank = True, null = True, related_name = "org_id")
	def __unicode__(self):
		return self.id_tei


class Manuscript(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	title = models.CharField("Title", max_length=100, blank = True)
	person_id = models.ForeignKey("Person", blank = True, null = True, related_name = "person_id_text")
	date = models.CharField("Date", max_length=20, blank = True)
	type_of_Manuscript =  models.CharField("Type", max_length=100, blank = True)
	call_no =  models.CharField("call_no", max_length=100, blank = True)
	def __unicode__(self):
		return self.title
	def get_type(self):
		return 'Manuscript'

class Page(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	Manuscript_id = models.ForeignKey("Manuscript", blank = True, null = True, related_name = "Manuscript_id")
	img_url = models.CharField("Image URL", max_length=200, blank = True)
	fulltext = models.TextField("Full Text", blank = True) #This might fail
	def __unicode__(self):
		return self.id_tei
	def get_type(self):
		return 'Page'

#Next time: Organization already existed... Whoops



#this one goes with the top 2 that were for testing
#was trying yo get things to work for foreign key fields but was struggling
"""
class Book(models.Model):

    name = models.CharField('Book name', max_length=100)
    author = models.ForeignKey(Person, blank=True, null=True)
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
            blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.name
"""
