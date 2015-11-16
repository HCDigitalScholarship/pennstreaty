from django.db import models

class Person(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	uri_lcnaf = models.CharField("URI LCNAF", max_length = 50)
	last_name = models.CharField("Last Name", max_length=100)
	first_name = models.CharField("First Name", max_length=100)
	middle_name = models.CharField("Middle Name", blank = True, max_length=100)
	other_names= models.TextField("Other Names", blank = True)
	birth_date = models.CharField("Birth Date", max_length=20, blank = True)
	death_date =  models.CharField("Death Date", max_length=20, blank = True)
	birth_place = models.ForeignKey("Place", blank = True, null = True, related_name = "birthplace")
	death_place = models.ForeignKey("Place", blank = True, null = True, related_name = "deathplace")
	gender =  models.CharField("Gender", blank = True, max_length=20)
	role = models.ForeignKey("RoleType", blank =True, null=True, related_name = '%(class)s_Role_1')
	role2 = models.ForeignKey("RoleType", blank = True, null= True, related_name = '%(class)s_Role_2')
	role3 = models.ForeignKey("RoleType", blank = True, null=True, related_name = '%(class)s_Role_3')
	affiliation =  models.CharField("Affiliation", blank = True, max_length=45) #do we want a model for affiliaiton?
	notes = models.TextField("Note Field", blank = True)
	PYM_index = models.TextField("PYM Index", blank = True)
	
	def __unicode__(self):
		return self.id_tei + " " + self.uri_lcnaf + " " + self.last_name + " " + self.first_name  + " " + self.middle_name + " " + self.other_names + " " + unicode(self.birth_date) +  " " + unicode(self.death_date) + " " + unicode(self.birth_place) + " " + unicode(self.death_place) + " " + self.gender + " " + unicode(self.role) + " " + unicode(self.role2) + " " + unicode(self.role3) + " " + self.affiliation + " " + self.notes + " " + self.PYM_index      


class Place(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	name = models.CharField("Name of Place", max_length = 100, blank = True)
	state = models.CharField("State", max_length = 20, blank = True)
	latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=6, blank = True, null = True)
	longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=6, blank = True, null = True)
	notes = models.TextField("Description Field", blank = True)
	PLACENAME = 'PN'
	GEOGNAME = 'GN'
	PLACE_TYPE_CHOICES = (
			(PLACENAME, 'Place Name'),
			(GEOGNAME, 'Geography Name'),
	)
   	place_type = models.CharField("Place Type", max_length=2, choices=PLACE_TYPE_CHOICES, default=PLACENAME, blank = True)
	alternate = models.TextField("Alternate Names", blank = True)

def __unicode__(self):
	return self.id_tei + " " + self.name + " " + self.state + " " + unicode(self.latitude) + " " + unicode(self.longitude) + " " + self.notes + " " + unicode(self.place_type) + " " + self.alternate

class Organization(models.Model):
	id_tei = models.CharField("TEI ID", max_length = 50)
	organization_name = models.CharField("Name of Organization", max_length = 100, blank = True)
	notes = models.TextField("Note Field", blank = True)
	associated_spellings = models.TextField("Associated Spellings/Names", blank = True)
	PYM_index = models.TextField("PYM Index", blank = True)

def __unicode__(self):
	return self.id_tei + " " + self.organization_name + " " + self.notes + " " + self.associated_spellings + " " + self.PYM_index



class RoleType(models.Model):
	role = models.CharField("Role_Type", max_length = 50, blank = True)
	description = models.TextField("Description of Role", blank = True)
	
	class Meta:
       		verbose_name_plural = "Role Types"
	
	def __unicode__(self):
		return self.role + " " + self.description