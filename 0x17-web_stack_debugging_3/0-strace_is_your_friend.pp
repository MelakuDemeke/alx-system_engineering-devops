# fix 500 error on wordpress site

exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
