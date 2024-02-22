# fix huge amount of failed requests.
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 2000\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart'
}
