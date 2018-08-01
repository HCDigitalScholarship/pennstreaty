# Beyond Penn's Treaty Project

This peoject by the Haverford DS Team that will serve as the adjunct, and then final site for all digital research and transcription done on Beyond Penn's Treaty. It  provides access to linked and annotated versions of Quaker diaries, letters, and meeting records which record contact with American Indians, particularly the Seneca, beginning in the 1740s.This application makes it possible to search across our Quaker-related projects for people, organizations and places. 


The backend of this site uses the Django framework (documentation can be found at https://www.djangoproject.com/), and PostgreSQL for database

The frontend of this site uses Foundation5 (the complete download). The documentation for Foundation can be found at http://foundation.zurb.com/develop/download.html.
Some other frontend features use Bootstrap4. Documentation for Bootstrap can be found at https://getbootstrap.com/docs/4.1/getting-started/introduction/


The features/visualizations on this site were made using the following libraries:

- [JQuery](http://jquery.com/)
- [DataTables](https://www.datatables.net/)
- [StoryMapJS](https://storymap.knightlab.com/advanced/)
- [Haystack Search](https://django-haystack.readthedocs.io/en/v2.8.1/tutorial.html) & [Solr, Search Engine](http://django-haystack.readthedocs.io/en/master/installing_search_engines.html)
- [CartoLocation for Overviewmaps](https://carto.com/)
 
Template for manuscript page view of this site are borrowed from [The Shelley - Godwin Archive project](http://shelleygodwinarchive.org/sc/bl/hymn_to_intellectual_beauty/#/p2)

## Read before you start
To learn more about how to get started with Django visit [Django website](https://docs.djangoproject.com/en/2.0/) and [Haverford Digital Scholarship CookBook Entry on Django](https://github.com/HCDigitalScholarship/ds-cookbook/blob/master/Djangology101.md),

for details about how to use and build this site and some features, please visit wiki page here:
https://github.com/HCDigitalScholarship/QI/wiki

### For Developers:
#### Read　[Wiki](https://github.com/HCDigitalScholarship/QI/wiki)
#### If you want to make modifications on templates, [this page](https://github.com/HCDigitalScholarship/QI/wiki/Templates-Explanation) in Wiki should be helpful to give you some directions.
#### **For future developers of this project: Please read wiki for [existing issues](https://github.com/HCDigitalScholarship/QI/wiki/Issues-and-Suggested-to-do-list) of this project and explanations on existing features**

### For Users:
#### Site map -- navigation of QI project:
[This page](https://github.com/HCDigitalScholarship/QI/wiki/Site-Map-Explanation) from our Wiki provides a detailed explanation for each feature of the project
#### Import manuscripts, StoryMap:

#### Review Unapproved Transcription:



### Excel Docs for Future Research on QI:

There is a shared google folder called quakers-and-indians which has the following types of information:

- Features/Website Functionality Spreadsheet
- TEI guidelines from SWAT
- TEI/XML files from SWAT
- Excel Docs on People, Places, Organizations (I've made jsons of these, and they are available in this`static/json folder)

Please ask Mike and/or Andy, and I'm sure they will be able to help you find the information/materials you need!


### Notes on using the importer:
- All spreadsheets need to have `id` as there first column and that column should be empty of data
- For places, categories should be `id,id_tei,name,county,state,latitude,longitude,notes,place_type,alternate,date`
- Need to do place,organization and then people, that order


### Notes on this README and Wiki:
**I have not gotten the time to explore every feature and detail of this project; therefore, a lot of documentaions are missing. <br/> To future developers, please update them.**
