#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "My Web Page Holberton" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
new="server_name _;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n"
sudo sed -i "s/server_name _;/$new/" /etc/nginx/sites-available/default
sudo service nginx restart
