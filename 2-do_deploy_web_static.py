#!/usr/bin/python3
"""
    deploye with fabric
"""

import os
from fabric.api import *
env.hosts = ['100.25.153.145', '35.174.185.38']


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
