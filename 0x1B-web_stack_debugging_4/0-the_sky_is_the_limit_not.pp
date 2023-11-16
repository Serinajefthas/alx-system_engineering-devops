#Script updates open file limit of nginx server to allow more requests to be managedi

file { '/etc/default/nginx':
    content => "ulimit -n 4096",
}
exec { 'restart_nginx':
    command => 'service nginx restart',
}
