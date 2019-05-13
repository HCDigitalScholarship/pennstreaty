import datetime
from haystack import indexes
from QI.models import Person, Place, Org, Page, Manuscript
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from haystack.query import SearchQuerySet

SearchQuerySet().filter(content='foo').models(Page)

class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True) # I think you use this for all indexes?
    uniqueID = indexes.CharField(model_attr='id_tei')
    firstname = indexes.CharField(model_attr='first_name', null=True, faceted=True) #Testing Faceting w/ This
    lastname = indexes.CharField(model_attr='last_name', null=True, faceted=True)
    middlename = indexes.CharField(model_attr='middle_name', null=True)
    displayname = indexes.CharField(model_attr='display_name', null=True)
    othernames = indexes.CharField(model_attr='other_names', null=True)
    birthdate = indexes.CharField(model_attr='birth_date', null=True, faceted=True)
    deathdate = indexes.CharField(model_attr='death_date', null=True, faceted=True)
    birthplace = indexes.CharField(model_attr='birth_place', null=True, faceted=True) #this is in the form of an id_tei (fix)
    deathplace= indexes.CharField(model_attr='death_place', null=True, faceted=True) #this is in the form of an id_tei (fix)
    gender = indexes.CharField(model_attr='gender', null=True)
    bionotes = indexes.CharField(model_attr='bio_notes', null=True)
    modeltype = indexes.CharField(model_attr='get_type', null=True)

    def get_model(self):
        return Person

    def get_type(self):
        return 'Person'


class PlaceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True) # I think you use this for all indexes?
    uniqueID = indexes.CharField(model_attr='id_tei')
    name = indexes.CharField(model_attr='name', null=True)
    county = indexes.CharField(model_attr='county', null=True, faceted=True)
    state = indexes.CharField(model_attr='state', null=True, faceted=True)
    notes = indexes.CharField(model_attr='notes', null=True)
    modeltype = indexes.CharField(model_attr='get_type', null=True)

    def get_model(self):
        return Place

    def get_type(self):
        return 'Place'


class OrgIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    uniqueID = indexes.CharField(model_attr='id_tei')
    name = indexes.CharField(model_attr='organization_name', null=True)
    place_id = indexes.CharField(model_attr='place_id', null=True, faceted=True)
    notes = indexes.CharField(model_attr='notes', null=True)
    associated_spellings = indexes.CharField(model_attr='associated_spellings', null=True)
    other_names = indexes.CharField(model_attr='other_names', null=True)
    date_founded = indexes.CharField(model_attr='date_founded', null=True, faceted=True)
    date_dissolved = indexes.CharField(model_attr='date_dissolved', null=True, faceted=True)
    org_type = indexes.CharField(model_attr='org_type', null=True, faceted=True)
    bio_notes = indexes.CharField(model_attr='bio_notes', null=True)
    modeltype = indexes.CharField(model_attr='get_type', null=True)

    def get_model(self):
        return Org

    def get_type(self):
        return 'Organization'


class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    uniqueID = indexes.CharField(model_attr='id_tei')
    manuscript = indexes.CharField(model_attr='Manuscript_id', null=True, faceted=True)  #this isn't in the database...??
    fulltext = indexes.CharField(model_attr='fulltext')
    modeltype = indexes.CharField(model_attr='get_type', null=True)
    # add more attributes here! (comment them out if data not in database yet)

    def get_model(self):
        return Page

    def get_type(self):
        return 'Page'


class ManuscriptIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    uniqueID = indexes.CharField(model_attr='id_tei')
    title = indexes.CharField(model_attr='title', null=True)
    person_id = indexes.CharField(model_attr='person_id', null=True, faceted=True)
    date = indexes.CharField(model_attr='date', null=True, faceted=True)
    type_of_Manuscript = indexes.CharField(model_attr='type_of_Manuscript', null=True, faceted=True)
    call_no = indexes.CharField(model_attr='call_no', null=True)
    modeltype = indexes.CharField(model_attr='get_type', null=True)
    # add more attributes here! (comment them out if data not in database yet)

    def get_model(self):
        return Manuscript

    def get_type(self):
        return 'Manuscript'

