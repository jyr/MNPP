#!/bin/sh
#
# php-fpm - this script starts and stops the php-fpm daemon
#
# chkconfig: - 85 15
# description: PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI \
#              implementation with some additional features useful for sites of \
#              any size, especially busier sites.
# processname: php-fpm

if [ $1 == 53 ];then
  php_fpm_CONF=/Applications/MNPP/conf/fpm/php-fpm.conf
else
  php_fpm_CONF=/Applications/MNPP/conf/php52/php-fmp
fi

prefix=/Applications/MNPP/Library/php$1
exec_prefix=${prefix} 
php_fpm_BIN=${exec_prefix}/sbin/php-fpm
php_fpm_PID=/Applications/MNPP/run/php-fpm.pid
 
php_opts="--fpm-config $php_fpm_CONF"
 
wait_for_pid () {
    try=0
 
    while test $try -lt 35 ; do
 
        case "$1" in
            'created')
            if [ -f "$2" ] ; then
                try=''
                break
            fi
            ;;
 
            'removed')
            if [ ! -f "$2" ] ; then
                try=''
                break
            fi
            ;;
        esac
 
        echo -n .
        try=`expr $try + 1`
        sleep 1
 
    done
 
}

__create_alias( ) {
    if [ ! -d "/usr/local/mysql" ]; then
        ln -s /Applications/MNPP/Library/mysql /usr/local/mysql
    fi
}

__set_privilegies( ) {
   chown -R mysql:mysql /usr/local/mysql/
   chown -R mysql:mysql /Applications/MNPP/tmp/mysql
}

__hosts( ){
  sh /Applications/MNPP/init/hosts.sh --add mnpp.astrata.local
  sh /Applications/MNPP/init/hosts.sh --add phpmyadmin.local
}

__export_library( ){
    export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/lib:$DYLD_LIBRARY_PATH
}

__show_usage( ) {
 
  echo "Usage: ${0} {53|52} {start|stop|quit|restart|reload|logrotate}"
  exit 1
}

__create_alias
__set_privilegies
__hosts
__export_library

if [ $1 == 53 ];then
  case "$2" in
      start)
          echo -n "Starting php-fpm "

          $php_fpm_BIN $php_opts

          if [ "$?" != 0 ] ; then
              echo " failed"
              exit 1
          fi

          wait_for_pid created $php_fpm_PID

          if [ -n "$try" ] ; then
              echo " failed"
              exit 1
          else
              echo " done"
          fi
      ;;

      stop)
          echo -n "Gracefully shutting down php-fpm "

          if [ ! -r $php_fpm_PID ] ; then
              echo "warning, no pid file found - php-fpm is not running ?"
              exit 1
          fi

          kill -QUIT `cat $php_fpm_PID`

          wait_for_pid removed $php_fpm_PID

          if [ -n "$try" ] ; then
              echo " failed. Use force-exit"
              exit 1
          else
              echo " done"
          fi
      ;;

      force-quit)
          echo -n "Terminating php-fpm "

          if [ ! -r $php_fpm_PID ] ; then
              echo "warning, no pid file found - php-fpm is not running ?"
              exit 1
          fi

          kill -TERM `cat $php_fpm_PID`

          wait_for_pid removed $php_fpm_PID

          if [ -n "$try" ] ; then
              echo " failed"
              exit 1
          else
              echo " done"
          fi
      ;;

      restart)
          $0 stop
          $0 start
      ;;

      reload)

          echo -n "Reload service php-fpm "

          if [ ! -r $php_fpm_PID ] ; then
              echo "warning, no pid file found - php-fpm is not running ?"
              exit 1
          fi

          kill -USR2 `cat $php_fpm_PID`

          echo " done"
      ;;

      *)
          __show_usage
      ;;

  esac
else
  case "${2}" in
      start|stop|quit|restart|reload|logrotate)
          /Applications/MNPP/Library/php52/sbin/php-fpm ${2}
          ;;
      *)
        __show_usage
        ;;
  esac
fi