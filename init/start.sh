#/bin/sh

__init( ) {
    sh /Applications/MNPP/init/php.sh $1 start
    sh /Applications/MNPP/init/percona.sh start
    sh /Applications/MNPP/init/nginx.sh start
}

__init $1
