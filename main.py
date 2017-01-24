"""Main File"""
VERSION = ".1"
AUTHORS = ["Wade Marshall", "Talor Tolbert"]

def init():
    print("Black jack, version %s. Created by %s") % (VERSION, getAuthors())


def getAuthors():
    """Returns the list AUTHORS as a string"""
    authors = ""
    for x in AUTHORS:
        if x is AUTHORS[len(AUTHORS) - 1]:
            authors += "and "
        authors += "%s " % x
    return authors


init()
