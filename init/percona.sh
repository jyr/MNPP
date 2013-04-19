#/bin/sh

export TMPDIR=/tmp

__show_usage( ) {
 
  echo "Usage: ${0} {start|stop|restart}"
  exit 3
}

__set_privilegies( ) {
   chown -R mysql:mysql /Applications/MNPP/tmp/mysql
   chown -R mysql:mysql /Applications/MNPP/Library/mysql
   chmod -R 755 /Applications/MNPP/Library/mysql/*
   chmod 644 /Applications/MNPP/Library/mysql/my.cnf
}

case "${1}" in
    start)
	__set_privilegies
	/Applications/MNPP/Library/mysql/support-files/mysql.server start
        ;;
    stop)
	/Applications/MNPP/Library/mysql/support-files/mysql.server stop
        ;;
    restart)
	/Applications/MNPP/Library/mysql/support-files/mysql.server restart
        ;;
    *)
        __show_usage
        ;;
esac

