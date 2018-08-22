from django.db import models
from django.urls import reverse
# Note, if you can't import something, and are getting "Column 'id' not found in dataset" django really likes when you have an empty id column first. In fact, it likes it so much, it doesn't work without it.


# import a list delimited by semicolons
# Might be able to change what django/MySql uses for id field
#https://django-import-export.readthedocs.org/en/latest/getting_started.html


class Person(models.Model):
    review_status = models.CharField("TEI ID", max_length=100)
    id_tei = models.CharField("TEI ID", max_length=100)
    lcnaf_uri = models.CharField("URI LCNAF", max_length=100, blank=True)
    last_name = models.CharField("Last Name", max_length=100, blank=True)
    first_name = models.CharField("First Name", max_length=100, blank=True)
    middle_name = models.CharField("Middle Name", blank=True, max_length=100)
    display_name = models.CharField("Display Name", blank=True, max_length=100)
    other_names= models.TextField("Other Names", blank=True, max_length=100)
    birth_date = models.CharField("Birth Date", max_length=100, blank=True)
    death_date =  models.CharField("Death Date", max_length=100, blank=True)
    birth_place = models.ForeignKey("Place", blank=True, null=True, related_name="birthplace", on_delete=models.CASCADE)
    death_place = models.ForeignKey("Place", blank=True, null=True, related_name="deathplace", on_delete=models.CASCADE)
    gender =  models.CharField("Gender", blank=True, max_length=20)
    role = models.ForeignKey("RoleType", blank=True, null=True, related_name='%(class)s_Role_1',on_delete=models.CASCADE)
    role2 = models.ForeignKey("RoleType", blank=True, null=True, related_name='%(class)s_Role_2',on_delete=models.CASCADE)
    role3 = models.ForeignKey("RoleType", blank=True, null=True, related_name='%(class)s_Role_3',on_delete=models.CASCADE)
    affiliation1 = models.CharField("Affiliation 1", blank=True, max_length=45) #do we want a model for affiliaiton?
    affiliation2 = models.CharField("Affiliation 2", blank=True, max_length=45)
    notes = models.TextField("Note Field", blank=True, max_length=100)
    bio_notes = models.TextField("Biography Note Field", blank=True, max_length=100)
    data_notes = models.TextField("Data Note Field", blank=True, max_length=100)
    citations = models.TextField("Citations", blank=True, max_length=100)
    PYM_index = models.TextField("PYM Index", blank=True, max_length=100)
    affiliations = models.ManyToManyField('Org', blank=True)

    def get_type(self):
        return 'People'

    def __str__(self):
        return self.id_tei + " " + self.first_name+ " " + self.last_name # + " " + self.uri_lcnaf + " " + self.last_name + " " + self.first_name  + " " + self.middle_name + " " + self.display_name + " " + self.other_names + " " + unicode(self.birth_date) +  " " + unicode(self.death_date) + " " + unicode(self.birth_place.name) + " " + unicode(self.death_place) + " " + self.gender + " " + unicode(self.role) + " " + unicode(self.role2) + " " + unicode(self.role3) + " " + self.affiliation1 + " " + self.affiliation2 + " " + self.notes + " " + self.bio_notes + " " + self.data_notes + " " + self.citations + " "  + unicode(self.PYM_index)


class Place(models.Model):
    id_tei = models.CharField("TEI ID", max_length=100)
    name = models.CharField("Name of Place", max_length=200, blank=True)
    county = models.CharField("County", max_length=100, blank=True)
    state = models.CharField("State", max_length=100, blank=True)
    latitude = models.CharField("Latitude", max_length=100, blank=True, null=True)
    longitude = models.CharField("Longitude", max_length=100, blank=True, null=True)
    notes = models.TextField("Description Field", max_length=500, blank=True)
    notes2 = models.TextField("Description Field", max_length=500, blank=True)
    PLACENAME = 'placeName'
    GEOGNAME = 'geogName'
    PLACE_TYPE_CHOICES = (
        (PLACENAME, 'Place Name'),
        (GEOGNAME, 'Geography Name'),
    )
    place_type = models.CharField("Place Type", max_length=30, choices=PLACE_TYPE_CHOICES,
                                  default=PLACENAME, blank=True)
    alternate = models.TextField("Alternate Names", max_length=200, blank=True)
    location_id = models.ForeignKey("Location", blank=True, null=True, related_name='Location',on_delete=models.CASCADE)
    date = models.CharField("Date", max_length=100, blank=True)

    def get_type(self):
        return 'Places'

    def __str__(self):
        return self.id_tei + " " + self.name + " " + self.state + " " + str(self.latitude) \
             + " " + str(self.longitude) + " " + self.notes + " " + self.notes2 + " "  \
             + str(self.place_type) + " " + self.alternate


## Some dumb-dumb may have accidentally put in Org when Organization already existed, but I am not sure what from Organization we want to keep though
class Org(models.Model):
    id_tei = models.CharField("TEI ID", max_length=500) #all the others have this but it might be unneccessary
    organization_name = models.CharField("Name of Organization", max_length=500, blank=True)
    place_id =  models.ForeignKey("Place", blank=True, null=True, related_name="place_id",on_delete=models.CASCADE)
    notes = models.TextField("Note Field", max_length=500, blank=True)
    associated_spellings = models.TextField("Associated Spellings/Names", max_length=500,
                                            blank=True)
    PYM_index = models.TextField("PYM Index", max_length=500, blank=True)
    other_names =  models.CharField("Other Names of Organization", max_length=500, blank=True)
    date_founded = models.CharField("Date Founded", max_length=500, blank=True)
    date_dissolved = models.CharField("Date Founded", max_length=500, blank=True)
    # might need an associated places here
    org_type = models.CharField("Oraganization Type", max_length=70, blank=True)
    bio_notes = models.TextField("Description Field", max_length=500, blank=True)
    data_notes = models.CharField("LCNAF URI", max_length=500, blank=True)
    notes = models.CharField("Notes", max_length=500, blank=True)
    lcnaf_uri = models.CharField("LCNAF URI", max_length=500, blank=True)
    citations = models.TextField("Description Field", max_length=500, blank=True)

    def __str__(self):
        return self.id_tei + " " + self.organization_name + " " + self.notes + " " \
             + self.associated_spellings + " " + self.PYM_index

    def get_type(self):
        return 'Groups'


class RoleType(models.Model):
    role = models.CharField("Role_Type", max_length=50, blank=True)
    description = models.TextField("Description of Role", blank=True)

    def __str__(self):
        return self.role + " " + self.description

    class Meta:
        verbose_name_plural = "Role Types"


# Models describing relationship e.g. Dave | is the father of | Dylan
class Relationship(models.Model):
    id_tei = models.CharField("TEI ID", max_length=50) # all the others have this but it might be unneccessary
    subject_id = models.ForeignKey("Person", blank=True, null=True, related_name="subjectid",on_delete=models.CASCADE) # might want to change the related names and defaults
    relationship_type_id = models.ForeignKey("RelationshipType", blank=True, null=True,
                                             related_name="relationshipType",on_delete=models.CASCADE)
    object_id = models.ForeignKey("Person", blank=True, null=True, related_name="objectid",on_delete=models.CASCADE)

    def __str__(self):
        return unicode(self.subject_id) + " " + unicode(self.relationship_type_id) + " " \
             + unicode(self.object_id)


class RelationshipType(models.Model):
    id_tei = models.CharField("TEI ID", max_length=50) # all the others have this but it might be unneccessary
    relationship_type = models.CharField("Relationship Type", max_length=100, blank=True)

    def __unicode__(self):
        return self.relationship_type

class Location(models.Model):
    id_tei = models.CharField("TEI ID", max_length=50)
    name = models.CharField("Name of Place", max_length=200, blank=True)
    # Just followed example from old place lat/long, but this could also be ints or floats or
    # something like that if desired
    latitude = models.CharField("Latitude", max_length=15, blank=True, null=True)
    longitude = models.CharField("Longitude", max_length=15, blank=True, null=True)
    loc_type_id = models.ForeignKey("LocType", blank=True, null=True, related_name="LocationType",on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LocType(models.Model):
    id_tei = models.CharField("TEI ID", max_length=50)
    loc_type = models.CharField("Name of Place", max_length=200, blank=True)

    def __str__(self):
        return self.loc_type


# I think this one is unnecessary
class Affiliation(models.Model):
    id_tei = models.CharField("TEI ID", max_length=50)
    person_id =  models.ForeignKey("Person", blank=True, null=True, related_name="person_id",on_delete=models.CASCADE)
    org_id =  models.ForeignKey("Org", blank=True, null=True, related_name="org_id",on_delete=models.CASCADE)

    def __str__(self):
        return self.id_tei


class Manuscript(models.Model):
    id_tei = models.CharField("TEI ID", max_length=100)
    title = models.CharField("Title", max_length=300, blank=True)
    person_id = models.ForeignKey("Person", blank=True, null=True, related_name="person_id_text",on_delete=models.CASCADE)
    org_id = models.ForeignKey("Org", blank=True, null=True, related_name="org_id_text",on_delete=models.CASCADE)
    person_name = models.CharField("Author", max_length=100, blank=True)
    org_name = models.CharField("Organization", max_length=200, blank=True)
    date = models.CharField("Date", max_length=50, blank=True)
    location = models.CharField("Location", max_length=20, blank=True)
    type_of_Manuscript =  models.CharField("Type", max_length=100, blank=True)
    call_no =  models.CharField("call_no", max_length=100, blank=True)
    summary = models.CharField("summary", max_length=1000,blank=True)
    transcribed = models.BooleanField("Transcribed", default=True)
    def __str__(self):
        return self.title

    def get_type(self):
        return 'Manuscripts'

class Page(models.Model):
    id_tei = models.CharField("TEI ID", max_length=50)
    Manuscript_id = models.ForeignKey("Manuscript", blank=True, null=True,related_name="Manuscript_id",on_delete=models.CASCADE)
    img_url = models.CharField("Image URL", max_length=200, blank=True)
    fulltext = models.TextField("Full Text", blank=True) # This might fail
    transcribed = models.BooleanField("Transcribed", default=True)
    def __str__(self):
        return self.id_tei

    def get_type(self):
        return 'Pages'

class PendingTranscription(models.Model):
    transcription = models.TextField()
    author = models.CharField(max_length=50, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    doc = models.ForeignKey("Page", on_delete=models.CASCADE)

   #def get_absolute_url(self):
        #return "admin_review_transcription/%i/" % self.id
 
    #def get_absolute_url(self):  
        #return reverse('admin_review_transcription', )

    def __str__(self):
        if self.author:
            return 'Pending Transcription of {0.doc} by {0.author} at {0.uploaded}'.format(self)
        else:
            return 'Pending Transcription of {0.doc.id_tei} at {0.uploaded}'.format(self)

    def get_type(self):
        return 'PendingTranscription'

