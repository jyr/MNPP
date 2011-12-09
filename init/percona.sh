#/bin/sh

__show_usage( ) {
 
  echo "Usage: ${0} {start|stop}"
  exit 3
}


case "${1}" in
    start)
        /Applications/MNPP/Library/mysql/bin/mysqld_safe -u root --port=3306 --socket=/Applications/MNPP/tmp/mysql/mysql.sock --lower_case_table_names=0 --datadir=/Applications/MNPP/Library/mysql/var --pid-file=/Applications/MNPP/tmp/mysql/mysql.pid --log-error=/Applications/MNPP/logs/mysql_error_log --tmpdir=/Applications/MNPP/tmp/mysql & sleep 1; exit 0 
        ;;
    stop)
        /Applications/MNPP/Library/mysql/bin/mysqladmin -u root --socket=/Applications/MNPP/tmp/mysql/mysql.sock shutdown
        ;;
    *)
        __show_usage
        ;;
esac