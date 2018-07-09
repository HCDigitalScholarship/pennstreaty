"""fffQI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from django.urls import path

urlpatterns = [
    path('travelRoutes/$', views.travelRoutes, name="TravelRoutes"),
    path('travelRoutes/', include('QI.inner')),
    path('profiles/$', views.profiles, name="Person Profiles"),
    path('manuscripts/$', views.manuscripts, name="Manuscripts"),
    path('transcribe/$', views.transcribe, name="Transcribe"),
    path('about/', views.about, name="About Page"),
    path('', views.Home.as_view(), name='home'),
    path('admin/review_transcriptions/',
        staff_member_required(views.ReviewTranscriptionList.as_view()),
        name='admin_review_transcription_lists'),
    path('admin/review_transcriptions/<int:id>/', views.review_transcription,
        name='admin_review_transcriptions'),
    path('admin/', admin.site.urls),
    path('cornp1/', views.cornp1, name="Henry Cornplanter"),
    path('places/', views.places, name="Places page"),
    path('organizations/', views.organizations, name="Organizations page"),
    path('admin/add_a_storymap/',views.SMimport, name="StoryMapImporter"),
    path('admin/QI/add_a_storymap/',views.SMimport, name="StoryMapImporter"),
    path('person/(?P<id>\S+)/', views.person_detail, name="person_detail"),
    path('place/(?P<id>\S+)/', views.place_detail, name="place_detail"),
    path('org/(?P<id>\S+)/', views.org_detail, name="org_detail"),
    path('alltheinfo/', views.htmlinfo, name="testinfo"), #maybe irrelevant
    path('something/(?P<id>\S+)/', views.jsoninfo, name="testinfo2"),
    path('page/(?P<id>\S+_[0-9]{3})/$', views.pageinfo, name="page"),
    path('transcribepage/<int:id>\S+_[0-9]{3})/$', views.transcribe_info, name="page"),
    path('pageinfo/(?P<id>\S+_[0-9]{3})/$', views.newpageinfo, name="pageinfo"),
    path('pagetranscription/(?P<id>\S+_[0-9]{3})/$', views.pagetranscription, name="pagetranscription"),
    path('manuscriptinfo/<int:id>\S+)/', views.pagejsoninfo, name="pagejsoninfo"),
    path('admin/QI/XML_to_HTML',views.new_xml_import, name="XMLImporter"),
    path('admin/XML_to_HTML',views.new_xml_import, name="XMLImporter"),
    path('testsearch/$', views.testsearch, name='testsearch'), #maybe irrelevant
#   path('search/', include('haystack.urls')),
    path('manuscript/(?P<id>\S+)/', views.manu_detail, name="manu_detail"),
    path('overviewmap_traveler', views.overviewmap_traveler, name='traveler'),
    path('overviewmap_date', views.overviewmap_date, name='date'),
    path('overviewmap_residence', views.overviewmap_residence, name='residence'),
    path('overviewmap_popularlocations', views.overviewmap_popularlocations, name='overviewmap_popularlocations'),
    path('outputPagePDF/(?P<id>\S+)/', views.outputPagePDF, name="outputPagePDF"),
    path('outputPagePT/(?P<id>\S+)/', views.outputPagePT, name="outputPagePT"),
    path('outputManuPT/(?P<id>\S+)/', views.outputManuPT, name="outputManuPT"),
    path('outputAll/', views.outputAll, name="outputAll"),
    path('historicalbackground/', views.historicalbackground, name="historicalbackground"),
    path('usingthesite/', views.usingthesite, name="usingthesite"),
    path('^bibliography/', views.bibliography, name="bibliography"),
    path('credits/', views.credits, name="credits"),
    path('mapgallery/', views.mapgallery, name="mapgallery"),
    path('contact/', views.contact, name="contact"),
    path('contactSuccess/', views.contactSuccess, name="contactSuccess"),
    path('searchtext/',views.inText_search, name="inText_search"),

]

admin.site.site_header = 'Beyond Penns Treaty'
admin.site.index_title = 'Beyond Penns Treaty Administration'
