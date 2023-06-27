# setup new ubunu server with nginx using puppet

exec { 'update system':
    command => 'apt-get update',
}

package { 'nginx':
    ensure => 'installed',
    require => Exec['update system'],
}

file { '/var/www/html/index.html':
    content => 'Hello World',
}
