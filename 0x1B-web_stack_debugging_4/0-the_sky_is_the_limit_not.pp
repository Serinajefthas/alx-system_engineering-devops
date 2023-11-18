#Script updates open file limit of nginx server to allow more requests to be managed

exec { 'update-ulimit':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
}
exec { 'restart_nginx':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
