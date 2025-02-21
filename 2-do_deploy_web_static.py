#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers.
"""
from fabric.api import env, put, run
import os

# Define the web servers
env.hosts = ['100.25.110.154', '100.25.21.81']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Deploys the archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract archive filename and folder name
        file_name = os.path.basename(archive_path)
        file_no_ext = file_name.split(".")[0]
        release_path = f"/data/web_static/releases/{file_no_ext}"

        # Upload archive to /tmp/ directory on the server
        put(archive_path, "/tmp/")

        # Create the release directory
        run(f"mkdir -p {release_path}")

        # Extract the archive
        run(f"tar -xzf /tmp/{file_name} -C {release_path}")

        # Move contents from the extracted folder to the final location
        run(f"mv {release_path}/web_static/* {release_path}/")

        # Remove the original extracted folder
        run(f"rm -rf {release_path}/web_static")

        # Remove the uploaded archive file
        run(f"rm /tmp/{file_name}")

        # Remove old symlink and create a new one
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_path} /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
