# Fix problem of high amount of requests

# Define an 'exec' resource named 'replace' to use the shell provider.
# This resource runs a command to replace the ulimit value in the nginx configuration file.
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

# Define another 'exec' resource named 'restart' to restart the nginx service.
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
