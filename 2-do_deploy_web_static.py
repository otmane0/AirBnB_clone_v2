#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers.
"""
from fabric.api import env, put, run
import os

# Define web server IPs
env.hosts = ['100.25.110.154', '100.25.21.81']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Deploys an archive to the web servers"""

    if not os.path.exists(archive_path):
        return False  # If the archive does not exist, return False

    try:
        # Extract filename without extension
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]  # web_static_XXXXXXXXXXXX

        # Define paths
        path = "/data/web_static/releases/"

        # Upload archive to /tmp/ on the server
        put(archive_path, '/tmp/')

        # Create the release directory
        run('mkdir -p {}{}/'.format(path, no_ext))

        # Extract the archive in the release directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))

        # Remove the archive from /tmp/
        run('rm /tmp/{}'.format(file_n))

        # Move contents to correct location
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))

        # Remove the now empty web_static directory
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        return True

    except Exception as e:
        return False