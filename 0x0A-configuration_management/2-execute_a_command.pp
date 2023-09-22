#kills process 'killmenow' using pkill cmd
exec { 'pkill':
  command     => 'pkill killmenow',
  provider    => 'shell',
  onlyif      => 'pgrep killmenow', #check that process killmenow exists
  path        => ['/bin', '/usr/bin'], #path puppet agent find pkill, pgrep
}
