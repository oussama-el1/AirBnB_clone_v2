#!/usr/bin/python3
"""
use Fabric to create archive
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
