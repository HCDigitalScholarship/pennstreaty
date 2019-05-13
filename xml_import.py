"""Convert TEI-encoded XML into human-readable HTML."""
import os
import sys

from lxml import etree, sax

from .models import Page, Manuscript


XSLT_DIR = os.path.dirname(os.path.realpath(__file__))
def if_already_exists(fsock):
    manuscript_id = os.path.splitext(fsock.name)[0]
    try:
        exist = True
        manuscipt= Manuscript.objects.get(id_tei=manuscript_id)
    except:
        exist = False
    return exist

def import_xml_from_file(fsock):
    manuscript_id = os.path.splitext(fsock.name)[0]
    data = fsock.read()
    html_tree = xml_to_html(etree.XML(data))
    try:
        manuscript = Manuscript.objects.get(id_tei=manuscript_id)
    # Delete preexisting pages associated with the manuscript.
        Page.objects.filter(Manuscript_id=manuscript).delete()
    except:
        manuscript= Manuscript.objects.create(id_tei=manuscript_id)

    for i, page in enumerate(html_tree.getroot()):
        transcription = etree.tostring(page, encoding='unicode', method='html')
        page_id = manuscript_id + '_' + str(i+1).rjust(3, '0')
        #Page(id_tei=page_id, fulltext=transcription, Manuscript_id=manuscript_id).save()
        Page.objects.create(id_tei=page_id, fulltext=transcription, Manuscript_id=manuscript)


class AugmentedContentHandler(sax.ElementTreeContentHandler):
    """Augment the lxml implementation to support better error messages and provide the useful
       (though namespace-unaware) startElement and endElement methods.
    """

    def __init__(self, *args, **kwargs):
        # Apparently I can't use super here because it's an old-style class.
        sax.ElementTreeContentHandler.__init__(self, *args, **kwargs)
        self.real_tag_stack = []

    def startElement(self, name, attributes=None):
        if attributes is not None:
            attributes = {(None, key): val for key, val in attributes.items()}
        AugmentedContentHandler.startElementNS(self, (None, name), name, attributes)

    def endElement(self, name):
        AugmentedContentHandler.endElementNS(self, (None, name), name)

    def startElementNS(self, ns_name, qname, attributes=None):
        self.real_tag_stack.append(qname)
        sax.ElementTreeContentHandler.startElementNS(self, ns_name, qname, attributes)

    def endElementNS(self, ns_name, qname):
        try:
            sax.ElementTreeContentHandler.endElementNS(self, ns_name, qname)
            self.real_tag_stack.pop()
        except sax.SaxError as e:
            msg = 'Tried to close <{}>'.format(qname)
            if self.real_tag_stack:
                msg += ', but last opened tag was <{}>'.format(self.real_tag_stack[-1])
            else:
                msg += ', but no tags have been opened'
            raise sax.SaxError(msg)


class TEIPager(AugmentedContentHandler):
    """A SAX parser that transforms <pb/> and <cb/> tags into <div>s that wrap pages and columns,
       respectively.
    """

    def __init__(self, *args, **kwargs):
        # Can't use super here because AugmentedContentHandler is an old-style class.
        AugmentedContentHandler.__init__(self, *args, **kwargs)
        # The tag stack is a stack of (ns_name, qname, attributes) tuples that represent the 
        # current path in the tree.
        self.tag_stack = []
        self.page = 0

    def startElementNS(self, ns_name, qname, attributes=None):
        if tag_eq(qname, 'pb'):
            self.handlePageBreak()
        elif tag_eq(qname, 'body'):
            self.startElement('div')
            self.startNewPageDiv()
        else:
            self.tag_stack.append( (ns_name, qname, attributes) )
            AugmentedContentHandler.startElementNS(self, ns_name, qname, attributes)

    def handlePageBreak(self):
        self.page += 1
        # In this project, TEI files have an initial page break that does not actually correspond
        # to a new page, so the actions for creating a new page should only be taken after the
        # first page break has been seen so that a spurious blank first page is not created for
        # every manuscript.
        if self.page > 1:
            self.closeAllTags()
            self.endElement('div')
            self.startNewPageDiv()
            self.reopenAllTags()

    def startNewPageDiv(self):
        self.startElement('div', {'class': 'tei-page'})

    def endElementNS(self, ns_name, qname):
        # Ignore self-closing <pb> tags; they were already handled by startElementNS.
        if tag_eq(qname, 'body'):
            self.endElement('div')
            self.endElement('div')
        elif not tag_eq(qname, 'pb'):
            closes = self.tag_stack.pop()
            try:
                AugmentedContentHandler.endElementNS(self, ns_name, qname)
            except sax.SaxError as e:
                raise sax.SaxError(str(e) + 'on page {0.page}'.format(self))

    def closeAllTags(self):
        for ns_name, qname, _ in reversed(self.tag_stack):
            AugmentedContentHandler.endElementNS(self, ns_name, qname)

    def reopenAllTags(self):
        for ns_name, qname, attributes in self.tag_stack:
            AugmentedContentHandler.startElementNS(self, ns_name, qname, attributes)


def xml_to_html(xml_root):
    """Convert the TEI-encoded XML document to an HTML document."""
    return paginate(preprocess(xml_root))


def preprocess(root):
    """Apply the XSLT stylesheet to the TEI-encoded XML document, but do not paginate."""
    xslt_path = os.path.join(XSLT_DIR, 'transform.xslt')
    xslt_transform = etree.XSLT(etree.parse(xslt_path).getroot())
    return xslt_transform(root)


def paginate(root):
    """Paginate the TEI-encoded XML document. This entails removing all <pb/> elements and adding
       <div class="page">...</div> elements to wrap each page. This function should be called
       after preprocessing.
    """
    handler = TEIPager()
    sax.saxify(root, handler)
    return handler.etree


def tag_eq(tag_in_document, tag_to_check):
    """Compare equality of tags ignoring namespaces. Note that this is not commutative."""
    return tag_in_document == tag_to_check or tag_in_document.endswith(':' + tag_to_check)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fsock:
        data = fsock.read()
    root = etree.XML(data)
    html_tree = xml_to_html(root)
    with open('/tmp/output.html', 'w') as fsock:
        fsock.write(etree.tostring(html_tree, encoding='unicode', method='html'))
