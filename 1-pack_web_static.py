#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the web_static folder.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from web_static folder."""

    # Step 1: Create the versions directory if it doesn’t exist
    local("mkdir -p versions")

    # Step 2: Generate a timestamp for the archive name
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = f"versions/{archive_name}"

    # Step 3: Create the .tgz archive
    result = local(f"tar -cvzf {archive_path} -C web_static .", capture=True)
    if result.succeeded:
        return archive_path
    else:
        return None

