# raise ulimit using sed
exec { 'debug':
  command  => 'sed -i "s/15/5000/g" /etc/default/nginx',
  provider => 'shell'
  path     => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec { 'restart':
  command  => 'sudo service nginx restart'
  provider => 'shell',
}