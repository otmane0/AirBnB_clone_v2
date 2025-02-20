#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """function do pack that generate .tgz"""
    local("mkdir -p versions > /dev/null 2>&1")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archiv = f"web_static_{timestamp}.tgz"
    archive_path = f"versions/{archiv}"
    result = local(f"tar -cvzf {archive_path} -C ~/alx/AirBnB_clone_v2/web_static .", capture=True)

    if result.succeeded:
        return archive_path
    else:
        return None



# local	# execute a local command)
# run	# execute a remote command on all specific hosts, user-level permissions)
# sudo	# sudo a command on the remote server)
# put	# copy over a local file to a remote destination)
# get	# download a file from the remote server)
# prompt	# prompt user with text and return the input (like raw_input))
# reboot	# reboot the remote system, disconnect, and wait for wait seconds)

