README for Beyond Penn's Treaty Project
Django Side of Project
Fall 2015

At the moment, this site uses the built in,light-weight SQLite database that comes with Django. 

The backend of this site uses the Django framework (documentation can be found at https://www.djangoproject.com/).

The frontend of this site uses Foundation5 (the complete download). The documentation for Foundation can be found at http://foundation.zurb.com/develop/download.html.

The features/visualizations on this site were made using the following libraries:

-JQuery (http://jquery.com/)
-DataTables (https://www.datatables.net/)
-StoryMapJS (https://storymap.knightlab.com/advanced/)

To learn more about how I got started with Django, Foundation, and creating the QMH site, please visit my wiki page on github here: https://github.com/HCDigitalScholarship/FriendsAsylum/wiki/Welcome-and-Introduction-to-QMH-and-Django

Excel Docs for Future Research on QI:

There is a shared google folder called quakers-and-indians which has the following types of information:

-Features/Website Functionality Spreadsheet
-TEI guidelines from SWAT
-TEI/XML files from SWAT
-Excel Docs on People, Places, Organizations (I've made jsons of these, and they are available in this repo's static>json folder)

Please ask Mike and/or Laurie, and I'm sure they will be able to help you find the information/materials you need!


Notes on using the importer:
-All spreadsheets need to have 'id' as there first column and that column should be empty of data
-For places, categories should be "id,id_tei,name,county,state,latitude,longitude,notes,place_type,alternate,date"
-Need to do place,organization and then people, that order


