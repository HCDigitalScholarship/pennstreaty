# Beyond Penn's Treaty Project

This peoject  by the Haverford DS Team that will serve as the adjunct, and then final site for all digital research and transcription done on Beyond Penn's Treaty. It  provides access to linked and annotated versions of Quaker diaries, letters, and meeting records which record contact with American Indians, particularly the Seneca, beginning in the 1740s.This application makes it possible to search across our Quaker-related projects for people, organizations and places. 


The backend of this site uses the Django framework (documentation can be found at https://www.djangoproject.com/).

The frontend of this site uses Foundation5 (the complete download). The documentation for Foundation can be found at http://foundation.zurb.com/develop/download.html.

The features/visualizations on this site were made using the following libraries:

- [JQuery](http://jquery.com/)
- [DataTables](https://www.datatables.net/)
- [StoryMapJS](https://storymap.knightlab.com/advanced/)
- [Haystack Search](https://django-haystack.readthedocs.io/en/v2.8.1/tutorial.html)
- [CartoLocation for Overviewmaps](https://carto.com/)
 
To learn more about how I got started with Django, Foundation, and creating the QMH site, please visit my wiki page on github here: 
https://github.com/HCDigitalScholarship/FriendsAsylum/wiki/Welcome-and-Introduction-to-QMH-and-Django

To learn more  about how to get started with Django, QI site and functionalities on this app please visit wiki page here:
https://github.com/HCDigitalScholarship/QI/wiki

### For Users:
#### import manscripts, Storymap:
#### Review unapproved Transcription:

### For Developers:


### Excel Docs for Future Research on QI:

There is a shared google folder called quakers-and-indians which has the following types of information:

- Features/Website Functionality Spreadsheet
- TEI guidelines from SWAT
- TEI/XML files from SWAT
- Excel Docs on People, Places, Organizations (I've made jsons of these, and they are available in this repo's `static/json` folder)

Please ask Mike and/or Andy, and I'm sure they will be able to help you find the information/materials you need!


### Notes on using the importer:
- All spreadsheets need to have `id` as there first column and that column should be empty of data
- For places, categories should be `id,id_tei,name,county,state,latitude,longitude,notes,place_type,alternate,date`
- Need to do place,organization and then people, that order


