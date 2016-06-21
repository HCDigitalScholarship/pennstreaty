import datetime
from haystack import indexes
from QI.models import Person #for the sake of this example
from QI.models import Place
from QI.models import Org
from QI.models import Page
from QI.models import Manuscript

class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True) #i think you use this for all indexes?
    uniqueID = indexes.CharField(model_attr='id_tei')
    firstname = indexes.CharField(model_attr='first_name')
    lastname = indexes.CharField(model_attr='last_name')
    """
    middlename = indexes.CharField(model_attr='middle_name')
    displayname = indexes.CharField(model_attr='display_name')
    othernames = indexes.CharField(model_attr='other_names')
    birthdate = indexes.CharField(model_attr='birth_date')
    deathdate = indexes.CharField(model_attr='death_date')
    birthplace = indexes.CharField(model_attr='birth_place') #this is in the form of an id_tei (fix)
    deathplace= indexes.CharField(model_attr='death_place') #this is in the form of an id_tei (fix)
    gender = indexes.CharField(model_attr='gender')
    bionotes = indexes.CharField(model_attr='bio_notes')
    """
    def get_model(self):
        return Person

class PlaceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True) #i think you use this for all indexes?
    uniqueID = indexes.CharField(model_attr='id_tei')
    name = indexes.CharField(model_attr='name')
    """
    county = indexes.CharField(model_attr='county')
    state = indexes.CharField(model_attr='state')
    latitude = indexes.CharField(model_attr='latitude')
    longitude = indexes.CharField(model_attr='longitude')
    notes = indexes.CharField(model_attr='notes')
    """
    def get_model(self):
        return Place

class OrgIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    uniqueID = indexes.CharField(model_attr='id_tei')
    name = indexes.CharField(model_attr='organization_name')
    # add more attributes here! (comment them out if data not in database yet)
    def get_model(self):
        return Org

class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    uniqueID = indexes.CharField(model_attr='id_tei')
    #manuscript = indexes.CharField(model_attr='Manuscript_id')  #this isn't in the database...??
    fulltext = indexes.CharField(model_attr='fulltext')
    # add more attributes here! (comment them out if data not in database yet)
    def get_model(self):
        return Page

class ManuscriptIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    uniqueID = indexes.CharField(model_attr='id_tei')
    title = indexes.CharField(model_attr='title')
    # add more attributes here! (comment them out if data not in database yet)
    def get_model(self):
        return Manuscript

#    def index_queryset(self, using=None):
#        """Used when the entire index for model is updated.""" #I don't know what this does?
#        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
