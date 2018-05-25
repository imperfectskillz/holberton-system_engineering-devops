# raise ulimit using sed
exec { 'debug':
  command  => 'sed -i "s/15/5000/g" /etc/default/nginx; sudo service nginx restart',
  provider => 'shell',
}