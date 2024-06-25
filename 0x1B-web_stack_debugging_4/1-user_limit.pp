# Change the OS configuration so that it is possible to login with the holberton user.

exec {'replace-after':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-before'],
}

exec {'replace-before':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf'
}
