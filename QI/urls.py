"""QI URL Configuration

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
from django.urls import path,re_path,reverse,include

app_name="QI"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(),name='home'),
    path('profiles', views.profiles, name="Person Profiles"),
    path('about', views.about, name="About Page"),
	path('base_explicit/', views.base_explicit, name='base explicit'), 
	path('base/', views.base, name='base non explicit'), 
    path('cornp1', views.cornp1, name="Henry Cornplanter"),
    path('places', views.places, name="Places page"),
    path('organizations', views.organizations, name="Organizations page"),
    path('manuscripts/', views.manuscripts, name="Manuscripts"),
    re_path(r'^page/(?P<id>\S+_[0-9]{3})', views.pageinfo, name="page"),
    re_path(r'^pageinfo/(?P<id>\S+_[0-9]{3})', views.newpageinfo, name="pageinfo"),
    re_path(r'^pagetranscription/(?P<id>\S+_[0-9]{3})', views.pagetranscription, name="pagetranscription"),
    path('travelRoutes/', views.travelRoutes, name="TravelRoutes"),
    path('travelRoutes/', include('QI.inner')),
    path('overviewmap_traveler', views.overviewmap_traveler, name='traveler'),
    path('overviewmap_date', views.overviewmap_date, name='date'),
    path('overviewmap_residence', views.overviewmap_residence, name='residence'),
    path('overviewmap_popularlocations', views.overviewmap_popularlocations, name='overviewmap_popularlocations'),
    path('historicalbackground', views.historicalbackground, name="historicalbackground"),
    path('usingthesite', views.usingthesite, name="usingthesite"),
    path('bibliography', views.bibliography, name="bibliography"),
    path('credits', views.credits, name="credits"),
    path('mapgallery', views.mapgallery, name="mapgallery"),
    path('contact', views.contact, name="contact"),
    path('contactSuccess', views.contactSuccess, name="contactSuccess"),
    path('admin/add_a_storymap',views.SMimport, name="StoryMapImporter"),
    path('admin/XML_to_HTML',views.new_xml_import, name="XMLImporter"),
    re_path(r'^person/(?P<id>\S+)/', views.person_detail, name="person_detail"),
    re_path(r'^place/(?P<id>\S+)/', views.place_detail, name="place_detail"),
    re_path(r'^org/(?P<id>\S+)/', views.org_detail, name="org_detail"),
    re_path(r'^something/(?P<id>\S+)', views.jsoninfo, name="testinfo2"),
    re_path(r'^manuscriptinfo/(?P<id>\S+)/', views.pagejsoninfo, name="pagejsoninfo"),
    re_path(r'^outputPagePT/(?P<id>\S+)/', views.outputPagePT, name="outputPagePT"),
    re_path(r'^outputManuPT/(?P<id>\S+)/', views.outputManuPT, name="outputManuPT"),
    re_path(r'^outputPagePDF/(?P<id>\S+)/', views.outputPagePDF, name="outputPagePDF"),
    path('outputAll', views.outputAll, name="outputAll"),
    path('search/',include('haystack.urls')), 
    path('transcribe', views.transcribe, name="Transcribe"),
    path('transcribepage/<id>', views.transcribe_info, name="transcribepage"),
    path('admin/review_transcriptions/',staff_member_required(views.ReviewTranscriptionList.as_view()),name='admin_review_transcription_lists'),
    path('admin/review_transcriptions/<int:pk>/', views.review_transcription,name='admin_review_transcriptions'),
    path('review_transcriptions', views.testing, name="testing"),
    path('inText_search', views.inText_search, name='searchInText'),
]


admin.site.site_header = 'Beyond Penns Treaty'
admin.site.index_title = 'Beyond Penns Treaty Administration'
