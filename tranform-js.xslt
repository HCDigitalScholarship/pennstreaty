<xsl:stylesheet version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
      xmlns:tei="http://www.tei-c.org/ns/1.0" 
      xmlns:msxsl="urn:schemas-microsoft-com:xslt"

 <msxsl:script language="JScript" implements-prefix="user">

  $(function(){

    $("#popoverInfo").popover({
        html : true,
        content: function() {
          return $('#popoverInfoContent').html();
        },
        title: function() {
          return $('#popoverInfoTitle').html();
        }
    });

});


 </msxsl:script>
</xsl:stylesheet>
