#!/usr/bin/python3
"""
Fabric script that send a folder from local machin to the server.
"""
import fabric.api as fab
import os


fab.env.hosts = ['100.25.110.154', '100.25.21.81']
fab.env.user = 'ubuntu'
fab.env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Generates a .tgz archive from web_static folder."""

    try:
        if not os.path.exists(archive_path):
            return False
        fab.put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1].split(".")[0]
        release_path = f"/data/web_static/releases/{file_name}"
        fab.run(f"sudo mkdir -p {release_path}")
        # Extract the archive
        fab.run(f"sudo tar -xvzf /tmp/{file_name}.tgz -C {release_path}")
        # Remove the old symlink
        fab.run("sudo rm -rf /data/web_static/current")
        fab.run(f"sudo ln -s /data/web_static/releases/{file_name} /data/web_static/current")
        return True
    except:
        # Any error, return False
        return False

