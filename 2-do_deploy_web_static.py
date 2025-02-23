#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers.
"""
from fabric.api import run, env, put, local, task
import os

# Define web server IPs
env.hosts = ["100.25.110.154", "100.25.21.81"]
user = "ubuntu"
key_path = "~/.ssh/school"

@task
def do_deploy(archive_path):
    """Deploys an archive to the web servers"""

    if not os.path.exists(archive_path):
        return False  # If the archive does not exist, return False

    try:
        # Extract filename without extension
        archive_name = os.path.basename(archive_path)  # with .tgz
        file_n = archive_name.split(".")[0]  # web_static_XXXXXXXXXXXX
        path = "/data/web_static/releases/"
        for server in env.hosts:
            # Establish connection
            env.host_string = f"{user}@{server}"
            put(archive_path, "/tmp/")  # Upload the archive
            run(f"tar -xvzf /tmp/{archive_name} -C /data/web_static/releases/{file_n}")  # Uncompress the archive
            run(f"rm -rf /tmp/{archive_name}")  # Delete the archive from the server
            run("rm -f /data/web_static/current")  # Delete the symbolic link
            run(f"ln -s /data/web_static/releases/{file_n} /data/web_static/current")  # Create the new symbolic link
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    do_deploy()


