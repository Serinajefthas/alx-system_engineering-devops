#kills process 'killmenow' using pkill cmd

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  path     => '/usr/bin/'
}
