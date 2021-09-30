#!/usr/bin/python3
"""Distributes an archive to the web servers,
using the function do_deploy:"""
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['35.227.117.239', '3.89.194.105']
env.key_filename = '~/.ssh/holberton'


def do_deploy(archive_path):
    """Distributes an archive to the web servers and sets up the new content
    """

    if not os.path.exists(archive_path):
        return False
    arc_name_ext = archive_path
    if '/' in archive_path:
        arc_name_ext = archive_path[archive_path.rindex('/') + 1:]
    arc_name = arc_name_ext
    if '.' in arc_name_ext:
        arc_name = arc_name[:arc_name.rindex('.')]

    with settings(warn_only=True):
        with cd('/tmp'):
            result = put(archive_path, arc_name_ext)
            if result.failed:
                return False

        new_release = '/data/web_static/releases/{}/'.format(arc_name)
        tmp_arc = '/tmp/{}'.format(arc_name_ext)
        current = '/data/web_static/current'

        results = [
            run('mkdir -p {}'.format(new_release)),
            run('tar -xzf {} -C {}'.format(tmp_arc, new_release)),
            run('rm {}'.format(tmp_arc)),
            run('mv {}web_static/* {}'.format(new_release, new_release)),
            run('rm -rf {}web_static'.format(new_release)),
            run('rm {}'.format(current)),
            run('ln -s {} {}'.format(new_release, current))
            ]
        if all(list(map(lambda r: r.succeeded, results))):
            print("New version Deployed!   0 errors")
            return True
    return False
