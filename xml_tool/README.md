At our college, we have several projects that involve digital images of archival documents.
These images are then used to transcribe the document.
We encode the text in XML/TEI for formatting and content types (typically language, persons, places, organizations). 

Problem: We currently have tools to transcribe (Omeka/Scripto) and to display completed
XML as HTML.  However, we do not have a unified workspace that allows web-users to access the 
images, transcribe the text and add XML encoding.   

I am looking to develop a Django and/or Javascript application that allows web-users to transcribe
text from an image and to easily add TEI/XML encoding to that text. 

If possible, I would like to use Vision API or other tools for OCR of the image.
  
While able to consult the original image, the user should be able to directly edit the XML, or switch to a 
simple text view.  The user could then highlight a name, for example, press 'n' and the application would add XML tags for <name>.  
Here's an example of this functionality (but running Tkinter): https://github.com/jiesutd/SUTDAnnotator
Here's another Java-based example: https://github.com/holloway/doctored 

The end-product is a Django application that allows for:
1) the display of an image using Open Sea Dragon (or comparable image viewer) on the left half of the screen (for example, see, https://ticha.haverford.edu/en/texts/Tl675a/)
2) the application should load the XML (example here: https://github.com/HCDigitalScholarship/ticha-xml-tei/blob/master/arte-cordova/ticha_arte.xml) 
3) an application window on the right that allows a user to toggle between the root XML
and text display for the page that corresponds to the displayed image.
4) it should be possible to edit the xml and save changes with versioning 
5) it should be possible to add markup to the text in the text display by highlighting
text and pressing a button or key (press 'n' for example to add <name> tags to selected text).

Projects currently running on Python 2.7, Ubuntu 14.04, Django 1.9.6

Components
	-Image Viewer
		- Open Sea Dragon, existing Ticha/Pennstreaty
		
	-Image OCR
		- add Vision API to project
		- send current image to API
		- send text to Mediawiki? to Db?
	
	-XML reader/display/editor (build from existing TichaMagic2, using Js libraries in Doctored)
		-open page XML for editing (+ Doctored) 
		-save revised XML to git (with SH or gittle, remote or local)
		-open xml as text (comparable to Doctored)
		-highlight text and add encoding (comparable to Doctored/SUTDAnnotator)
		-save revised text encoding to git (SH or gittle) 
