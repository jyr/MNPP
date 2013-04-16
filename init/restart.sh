#/bin/sh

__init( ) {
  sh /Applications/MNPP/init/php.sh $1 restart
  sh /Applications/MNPP/init/percona.sh restart
  sh /Applications/MNPP/init/nginx.sh restart
}

__init $1

