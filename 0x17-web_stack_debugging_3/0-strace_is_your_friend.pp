#Script to fix apache returning 500 internal server error
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  require => Package['nginx'], # Ensure Nginx package is installed before managing the file
}
exec { 'replace_sites_enabled':
  command     => 'sed -i s/sites-enabled/sites-available/g /etc/nginx/nginx.conf',
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
  notify      => Service['nginx'],
}
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['replace_sites_enabled'],
}
