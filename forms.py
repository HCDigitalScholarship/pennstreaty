from django import forms
from django.utils.translation import ugettext_lazy
from haystack.forms import SearchForm
from haystack.query import EmptySearchQuerySet, SearchQuerySet
from dal import autocomplete
from django.db import models
from QI.models import Manuscript
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Any concerns, comments, or questions you may have"


class ImportXMLForm(forms.Form):
    xml_file = forms.FileField(label='')

class TranscribeForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': ugettext_lazy('Enter your transcription here.'),'style': 'height:400px; width:100%'}))
    name = forms.CharField(label=ugettext_lazy('Name (optional)'), required=False, max_length=50)

class CaptchaForm(forms.Form):
    #field = AnyOtherField()
    captcha = CaptchaField()

