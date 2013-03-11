#/bin/sh

__init( ) {
  
  sh /Applications/MNPP/init/php.sh $1 stop
  sh /Applications/MNPP/init/percona.sh stop
  sh /Applications/MNPP/init/nginx.sh stop
}

__init $1
