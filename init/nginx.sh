#/bin/sh
 
NGINX_BASE_DIR="/Applications/MNPP/Library/nginx"
NGINX_DAEMON="${NGINX_BASE_DIR}/nginx"
NGINX_CONF="/Applications/MNPP/conf/nginx/nginx.conf"

__launch_signal( ) {
 
  ${NGINX_DAEMON} -s ${1} &>/dev/null
}
 
__checkconfig( ) {
 
  ${NGINX_DAEMON} -c ${NGINX_CONF} -t &>/dev/null
}
 
__start( ) {
 
  [ -r ${NGINX_CONF} ] || exit 1 
 
  __checkconfig && ${NGINX_DAEMON} -c ${NGINX_CONF} &>/dev/null || return ${?}
}
 
__stop( ) {
 
  __launch_signal stop
}
 
__reload( ) {
 
  __checkconfig && __launch_signar reload || return ${?}  
}
 
__restart( ) {
 
  __stop && __start
}
 
__show_usage( ) {
 
  echo "Usage: ${0} {start|stop|restart|reload}"
  exit 3
}
 
##
# :: main ::
case "${1}" in
  start|stop|restart|reload)
    [ -x ${NGINX_DAEMON} ] || exit 2
    __${1}
    ;;
  *)
    __show_usage
    ;;
esac
