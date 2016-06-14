import datetime
from haystack import indexes
from QI.models import Person #for the sake of this example

class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True) #i think you use this for all indexes?
    #i'm just going to pick some attributes to use from the Person model
    uniqueID = indexes.CharField(model_attr='id_tei')
    firstname = indexes.CharField(model_attr='first_name')
    lastname = indexes.CharField(model_attr='last_name')

    def get_model(self):
        return Person

#    def index_queryset(self, using=None):
#        """Used when the entire index for model is updated.""" #I don't know what this does?
#        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
