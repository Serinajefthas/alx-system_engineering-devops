# Script creates custom http header response but this time w Puppet
exec { 'cmd':
  command => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served_by $HOSTNAME;" /etc/nginx/sites_available/default;
  service nginx start',
  provider => shell,
}
