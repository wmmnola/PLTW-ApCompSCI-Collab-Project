"""Main File"""
import game
VERSION = ".1"
AUTHORS = ["Wade Marshall", "Talor Tolbert"]


def init():
    """Startup Function, everything should start here"""
    print("Black jack, version v%s. Created by %s") % (VERSION, getAuthors())
    print("Githug Repository: " +
          "https://github.com/wmmnola/PLTW-ApCompSCI-Collab-Project")
    print("This project is Licensed with the GPL 3.0 License.")
    print("Any attempt to redistribute this software as non-free software is" +
          " illegal`.")
    game.game_debug()


def getAuthors():
    """Returns the list AUTHORS as a string"""
    authors = ""
    for x in AUTHORS:
        if x is AUTHORS[len(AUTHORS) - 1]:
            authors += "and "
        authors += "%s" % x
        if x is AUTHORS[len(AUTHORS) - 1]:
            authors+=" "
        else:
            authors+= ", "
    return authors


init()
