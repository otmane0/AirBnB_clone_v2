#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
"""
import fabric.api as fab
from datetime import datetime


def do_pack():
    """function do pack that generate .tgz"""
    fab.local("ls versions > /dev/null 2>&1 || mkdir versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz = fab.local("tar -cvzf versions/web_static_{}.tgz web_static\
".format(date))
    if tgz.succeeded:
        return "versions/web_static_{}.tgz".format(date)
    return None
