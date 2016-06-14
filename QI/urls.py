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
from django.conf.urls import include, url, patterns
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^storymap/$', 'QI.views.storymap_dir', name = "StoryMapJS"),
    url(r'^storymap/', include('QI.inner')),
    url(r'^profiles/$', 'QI.views.profiles', name = "Person Profiles"),
	url(r'^texts/$', 'QI.views.texts', name = "Available Texts"),
	url(r'^about/$', 'QI.views.about', name = "About Page"),
    url(r'^$', views.Home.as_view(), name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cornp1/$', 'QI.views.cornp1', name = "Henry Cornplanter"),
    url(r'^places/$', 'QI.views.places', name = "Places page"),
    url(r'^organizations/$', 'QI.views.organizations', name = "Organizations page"),
    url(r'^admin/add_a_storymap/','QI.views.SMimport', name = "StoryMapImporter"),
    url(r'^admin/QI/add_a_storymap/','QI.views.SMimport', name = "StoryMapImporter"),
    url(r'^person/(?P<id>\S+)/', 'QI.views.person_detail', name = "person_detail"),
    url(r'^place/(?P<id>\S+)/', 'QI.views.place_detail', name = "place_detail"),
    url(r'^org/(?P<id>\S+)/', 'QI.views.org_detail', name = "org_detail"),
    url(r'^alltheinfo', 'QI.views.htmlinfo', name = "testinfo"), #maybe irrelevant
    url(r'^something/(?P<id>\S+)/', 'QI.views.jsoninfo', name = "testinfo2"),
    #url(r'^page/(?P<id>\S+)/', 'QI.views.pageinfo', name="pageinfo"),
    url(r'^page/(?P<id>\S+_[0-9]{3})/$', 'QI.views.pageinfo', name="page"),
    url(r'^pageinfo/(?P<id>\S+_[0-9]{3})/$', 'QI.views.newpageinfo', name="pageinfo"),
    url(r'^manuscriptinfo/(?P<id>\S+)/', 'QI.views.pagejsoninfo', name="pagejsoninfo"),
    url(r'^admin/QI/XML_to_HTML','QI.views.XMLimport', name = "XMLImporter"),
    url(r'^testsearch/$', 'QI.views.testsearch', name='testsearch'), #maybe irrelevant
    url(r'^search/', include('haystack.urls')),
]

admin.site.site_header = 'Beyond Penns Treaty'
admin.site.index_title = 'Beyond Penns Treaty Administration'
