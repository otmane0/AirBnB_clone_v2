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
        file_name = archive_path.split("/")[-1]
        file_no_ext = file_name.split(".")[0]  # web_static_XXXXXXXXXXXX

        # Define paths
        remote_path = f"/tmp/{file_name}"
        release_path = f"/data/web_static/releases/{file_no_ext}"

        # Upload archive to /tmp/ on the server
        put(archive_path, remote_path)

        # Create the release directory
        run(f"sudo mkdir -p {release_path}")

        # Extract the archive in the release directory
        run(f"sudo tar -xzf {remote_path} -C {release_path}")

        # Remove the archive from /tmp/
        run(f"sudo rm {remote_path}")

        # Move contents to correct location
        run(f"sudo mv {release_path}/web_static/* {release_path}/")

        # Remove the now-empty web_static directory
        run(f"sudo rm -rf {release_path}/web_static")

        # Delete old symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create new symbolic link
        run(f"sudo ln -s {release_path} /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
