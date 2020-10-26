from . models import *


def get_bibliography(ms_object):
    bibl = Zitat.object.filter(manuscript=ms_object)
    return bibl
