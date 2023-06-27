# setup new ubunu server with nginx using puppet

exec { 'update system':
command => 'apt-get update',
}

