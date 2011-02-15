#/bin/sh

__show_usage( ) {
 
  echo "Usage: ${0} {start|stop}"
  exit 3
}


case "${1}" in
    start)
        /Applications/MEPP/Library/mysql/bin/mysqld_safe -u root --port=3306 --socket=/Applications/MEPP/tmp/mysql/mysql.sock --lower_case_table_names=0 --datadir=/Applications/MEPP/Library/mysql/var --pid-file=/Applications/MEPP/tmp/mysql/mysql.pid --log-error=/Applications/MEPP/logs/mysql_error_log --tmpdir=/Applications/MEPP/tmp/mysql &
        ;;
    stop)
        /Applications/MEPP/Library/mysql/bin/mysqladmin -u root --socket=/Applications/MEPP/tmp/mysql/mysql.sock shutdown
        ;;
    *)
        __show_usage
        ;;
esac