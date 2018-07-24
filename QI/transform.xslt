<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:msxsl="urn:schemas-microsoft-com:xslt">
  <xsl:output omit-xml-declaration="yes" method="xhtml" indent="yes"/>


  <xsl:template match="/">
    <body>
      <xsl:apply-templates select="tei:TEI/tei:text" />
    </body>
  </xsl:template>


  <!-- Transform <head>. -->
  <xsl:template match="tei:head">
    <h4>
      <xsl:apply-templates/>
    </h4>
  </xsl:template>


  <!-- Transform <p>. -->
  <xsl:template match="tei:p">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>


  <!-- Transform <lb>. -->
  <xsl:template match="tei:lb">
    <br/>
  </xsl:template>

  <!-- Transform <persName>, <orgName>, <placeName> -->
  <xsl:template match="tei:persName">
    <a class="persName" id="Per-popover-{position()}" data-toggle="Person-popover-{position()}" data-trigger="fcours" data-popover-content="#a{position()}" data-placement="right">
      <xsl:attribute name="href">

        <xsl:text>#</xsl:text>
        <xsl:value-of select="@key" />
      </xsl:attribute>
      <xsl:apply-templates/>
    </a>
     <div id="a{position()}" class="hidden">
      <div id="Per-popover-header" class="hide">Person Information <span style="float:right;cursor:pointer;" class="fa fa-times" data-toggle="popover"></span>
      </div>
      <div id="Per-popover-body-{position()}" class="hide">
      </div>
    </div>
  </xsl:template>
  
  <xsl:template match="tei:orgName">
    <a class="orgName" id="Org-popover-{position()}" data-toggle="Orgnization-popover-{position()}" data-trigger="fcours" data-popover-content="#b{position()}" data-placement="right">
      <xsl:attribute name="href">
        <xsl:text>#</xsl:text>
        <xsl:value-of select="@key" />
      </xsl:attribute>
      <xsl:apply-templates/>
    </a>
    <div id="b{position()}" class="hidden">
      <div id="Org-popover-header">Orgnization Information <span style="float:right;cursor:pointer;" class="fa fa-times" data-toggle="popover"></span>
      </div>
      <div id="Org-popover-body-{position()}">
      </div>
    </div>
  </xsl:template>
 
  
  <xsl:template match="tei:placeName">
    <a class="placeName"  id="Pla-popover-{position()}" data-toggle="Place-popover-{position()}" data-trigger="fcours" data-popover-content="#c{position()}" data-placement="right">
      <xsl:attribute name="href">
        <xsl:text>#</xsl:text>
        <xsl:value-of select="@key" />
      </xsl:attribute>
      <xsl:apply-templates/>
    </a>
    <div id="c{position()}" class="hidden">
      <div id="Pla-popover-header">Place Inoformation <span style="float:right;cursor:pointer;" class="fa fa-times" data-toggle="popover"></span>
      </div>
      <div id="Pla-popover-body-{position()}">
      </div>
    </div>
  </xsl:template>


  <!-- Preserve these (without the TEI namespace). -->
  <xsl:template match="tei:pb|tei:div">
    <xsl:element name="{local-name()}">
      <xsl:copy-of select="@*"/>
      <xsl:apply-templates/>
    </xsl:element>
  </xsl:template>


  <!-- The namespace on xml:id has to be eliminated. -->
  <xsl:template match="tei:div[@xml:id]">
    <div>
      <xsl:attribute name="id">
        <xsl:value-of select="@xml:id" />
      </xsl:attribute>
      <xsl:apply-templates/>
    </div>
  </xsl:template>


  <!-- Ignore these but copy their contents. -->
  <xsl:template match="tei:pc|tei:i|tei:fw|tei:emph|tei:u|tei:hi|tei:gap|tei:text|tei:choice|tei:ref|tei:front|tei:body|tei:back|tei:g|tei:c|tei:add|tei:foreign">
    <xsl:apply-templates/>
  </xsl:template>


  <!-- Catch unmatched nodes (courtesy of stackoverflow.com/questions/3360017/). -->
  <xsl:template match="*">
    <xsl:message>STYLESHEET WARNING: unmatched element <xsl:value-of select="name()"/></xsl:message>
    <xsl:apply-templates/>
  </xsl:template>
</xsl:stylesheet>
