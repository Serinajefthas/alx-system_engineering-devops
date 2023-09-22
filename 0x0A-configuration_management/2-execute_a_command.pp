exec { 'kill_killmenow_process':
  command     => 'pkill -9 killmenow',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
  path        => ['/bin', '/usr/bin'], #path puppet agent find pkill, pgrep
}

