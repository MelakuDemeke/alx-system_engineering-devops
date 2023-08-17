# Fix problem of high amount files opened
# Define an 'exec' resource named 'replace-1' to use the shell provider.
# This resource runs a command to replace the 'nofile' limit value in the limits.conf file.
exec {'replace-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-2'],
}

# Define another 'exec' resource named 'replace-2' to replace another 'nofile' limit value in limits.conf.
exec {'replace-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
