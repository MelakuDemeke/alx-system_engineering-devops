# Fix problem of high amount of requests
# Define ulimit value and service name
$ulimit_value = '4096'
$service_name = 'nginx'

# Update ulimit value
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT=\"-n $ulimit_value\"\n",
  notify  => Exec['restart_service'],
}

# Restart the service when ulimit is updated
exec { 'restart_service':
  command     => "sudo service $service_name restart",
  refreshonly => true,
}
