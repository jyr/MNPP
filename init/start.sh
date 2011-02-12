#/bin/sh

__init( ) {
    sh /Applications/MEPP/init/php-fpm.sh start
    sh /Applications/MEPP/init/mysql.sh start
    sh /Applications/MEPP/init/nginx.sh start
}

__init
