# kills killmenow process
exec { 'killmenow':
  path    => ['/usr/bin', '/usr/sbin'],
  command => 'pkill -f killmenow'
}