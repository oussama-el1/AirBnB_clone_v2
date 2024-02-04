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
        pwe = os.path.splitext(packe_name)
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{pwe}/')
        run(f'tar -xzf /tmp/{packe_name} -C /data/web_static/releases/{pwe}/')
        run(f'rm /tmp/{packe_name}')
        path = '/data/web_static/releases/'
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, pwe))
        run('rm -rf {}{}/web_static'.format(path, pwe))
        run(f'rm /data/web_static/current')
        run(f'ln -s {path}{pwe}/ /data/web_static/current')
        return True
    except Exception as e:
        return False
