#!/usr/bin/env bash

dpkg -l | grep nginx  > /dev/null 2>&1 || (sudo apt -y update && sudo apt -y upgrade && sudo apt -y install nginx)

declare -a dirs=(
  "/data"
  "/data/web_static"
  "/data/web_static/releases"
  "/data/web_static/shared"
  "/data/web_static/releases/test"
)

for dir in "${dirs[@]}"; do
  [ ! -d "$dir" ] && sudo mkdir -p "$dir" > /dev/null 2>&1
done
touch "/data/web_static/releases/test/index.html"
ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

