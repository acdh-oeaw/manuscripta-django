from django.template.loader import render_to_string
from acdh_tei_pyutils.tei import TeiReader


def make_tei(item):
    rendered = render_to_string("archiv/tei_template.xml", {"object": item})
    doc = TeiReader(rendered)
    return doc.return_string()
