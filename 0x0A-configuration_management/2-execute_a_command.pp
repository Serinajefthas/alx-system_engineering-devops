#kills process 'killmenow' using pkill cmd
exec { 'pkill':
  command     => 'pkill -9 killmenow',
  provider    => 'shell',
  onlyif      => 'pgrep killmenow',
  path        => ['/bin', '/usr/bin'], #path puppet agent find pkill, pgrep
}
