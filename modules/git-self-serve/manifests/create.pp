define git-self-serve::create ( ) {

  file { 
    '/usr/local/etc/git-self-serve':
      ensure => directory,
      mode   => '0755',
      owner  => 'root',
      group  => 'root';
    '/usr/local/etc/git-self-server/repocron.py':
      mode   => '0755',
      owner  => 'www-data',
      group  => 'www-data'
      source => "puppet:///modules/git-self-server/repocron.py";	
	}

  cron { 'reporeq':
    command     => '/usr/local/etc/git-self-serve/repocron.py',
    user        => 'www-data',
    minute      => 30,
    environment => "PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin\nSHELL=/bin/sh", # lint:ignore:double_quoted_strings
    require     => Class['gitserver_asf'],
  }

}
