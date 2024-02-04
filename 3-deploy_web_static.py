#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir
import os
env.hosts = ['100.25.153.145', '35.174.185.38']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("exception here")
        return None


def do_deploy(archive_path):
    """deploy content"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        packe_name = os.path.basename(archive_path)
        pwe = packe_name.split(".")[0]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(pwe))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(packe_name, pwe))
        run('rm /tmp/{}'.format(packe_name))
        path = '/data/web_static/releases/'
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, pwe))
        run('rm -rf {}{}/web_static'.format(path, pwe))
        run('rm /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, pwe))
        return True
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
