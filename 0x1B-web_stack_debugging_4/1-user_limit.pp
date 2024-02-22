# Change the OS configuration so that it is possible to login with the holberton user.

exec {'replace-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 8/nofile 80000/" /etc/security/limits.conf',
  before   => Exec['replace-2'],
}

exec {'replace-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf'
}
