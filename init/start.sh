#/bin/sh

__init( ) {
    sh /Applications/MNPP/init/php-fpm.sh start
    sh /Applications/MNPP/init/mysql.sh start
    sh /Applications/MNPP/init/nginx.sh start
}

__init
