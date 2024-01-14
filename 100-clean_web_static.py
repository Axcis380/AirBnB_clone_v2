#!/usr/bin/python3
"""
Del out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['52.87.155.66', '54.89.109.87']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = int(number)

    with lcd("versions"):
        local_archives = sorted(os.listdir("."))
        local_archives_to_delete = local_archives[:-number]
        local("rm -f {}".format(" ".join(local_archives_to_delete)))

    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr | grep 'web_static_'", quiet=True).split()
        # Ensure we don't delete all archives if number exceeds available archives
        if number < len(remote_archives):
            remote_archives_to_delete = remote_archives[:-number]
            sudo("rm -rf {}".format(" ".join(remote_archives_to_delete)), quiet=True)

