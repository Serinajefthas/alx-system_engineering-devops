#Script updates open file limit of nginx server to allow more requests to be managedi

exec { 'update-ulimit':
    path    => '/usr/local/bin/:/bin/'
    command => "ulimit -n 4096",
}
exec { 'restart_nginx':
    command => 'service nginx restart',
}
