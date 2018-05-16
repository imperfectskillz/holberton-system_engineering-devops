# using puppet to change php to phpp
exec { 'replace phpp to php':
  command  => "/bin/sed -i -e 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  provider => 'shell',
}