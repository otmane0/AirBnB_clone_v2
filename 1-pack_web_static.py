#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the web_static folder.
"""
from invoke import run
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from web_static folder."""

    # Step 1: Create the versions directory if it doesn’t exist
    os.makedirs("versions", exist_ok=True)

    # Step 2: Generate a timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"

    # Step 3: Create the .tgz archive
    result = run(f"tar -cvzf {archive_path} web_static", hide=True, warn=True)

    # Step 4: Return the archive path if successful, otherwise None
    return archive_path if result.ok else None
