# Prepare your web serversr with puppet.

exec { 'Deploy server':
  command  => 'sudo apt-get -y update && sudo apt-get install nginx -y && sudo mkdir -p /data/web_static/releases/ && sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && sudo touch /data/web_static/releases/test/index.html && echo "My Web Page Holberton" > /data/web_static/releases/test/index.html && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -R ubuntu:ubuntu /data && str="server_name _;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n" && sudo sed -i "s/server_name _;/$str/" /etc/nginx/sites-available/default && sudo service nginx restart',
  provider => 'shell',
}
