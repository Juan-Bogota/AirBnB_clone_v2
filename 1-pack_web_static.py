#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
 web_static folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import local
from datetime import datetime

def do_pack():
     try:
          formato = "%Y%m%d%H%M%S"
          date_now = datetime.now()
          created_at = date_now.strftime(formato)
          local("mkdir -p versions")
          file_tgz = "web_static_{}.tgz".format(created_at)
          local("tar -cvzf versions/{} web_static".format(file_tgz))
          return file_tgz
     except:
          return None
