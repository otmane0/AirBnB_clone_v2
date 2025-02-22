#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
"""

from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:

        # Create the 'versions' directory if it doesn't exist
        if not os.path.exists("versions"):
            print("Creating 'versions' directory...")
            os.system("mkdir -p versions")

        # Generate the archive name using the current timestamp
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )
        archive_path = "versions/{}".format(archive_name)

        # Create the .tgz archive
        result = os.system("tar -cvzf {} -C web_static .".format(archive_path))

        # Check if the archive was created successfully
        if result == 0:  # tar command returns 0 on success
            return archive_path
        else:
            return None
    except Exception as e:
        return None

# Run the do_pack function
if __name__ == "__main__":
    do_pack()