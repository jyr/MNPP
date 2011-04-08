#!/bin/bash
#
#   Automatic nginx vhost generator
#
#   Iván Mayoral
#   ivan@astrata.com.mx
#
#   Modify by Jair Gaxiola
#   https://github.com/jyr

#------ Global vars -----

NGINX_BIN="/Applications/MNPP/Library/nginx/nginx"
NGINX_INIT="/Applications/MNPP/init/nginx.sh"
RESTART_CMD="sh ${NGINX_INIT} restart"

S_AVAILABLE="sites-available/"
S_ENABLED="sites-enabled/"
HTTP_PORT="80"
PHPFM_SERVER="127.0.0.1"
PHPFM_PORT="9000"
LOGS_DIR="/Applications/MNPP/logs/nginx/"
AUTO_DIR="common"
COMMON_DIR="/Applications/MNPP/conf/nginx/common/"


#--------------------------

# Usage example
if [[ "$@" = *-h* ]] || [[ $# = 0 ]]; then
  echo "Usage : init.sh HOSTNAME ROOT_DIR [ -drupal | -php | -mobile | -cake | -magento ]"
  exit 0
fi


# Try to retrieve conf from init.d
NGINX_CONF_FILE=`cat $NGINX_INIT | sed -n 's/^NGINX_CONF="\(.*\)".*/\1/p'`
NGINX_CONF_DIR=`dirname $NGINX_CONF_FILE`


# If fail, try to retrieve from bin's vars
if [ -z $NGINX_CONF_FILE ]; then
  NGINX_CONF_FILE=`$NGINX_BIN -V 2>&1 | sed -n 's/.*--conf-path=\([^\s]*\)\s.*/\1/p'`
  NGINX_CONF_DIR=`dirname $NGINX_CONF_FILE`
fi

# If fail again use daemon's route
if [ -z $NGINX_CONF_FILE ]; then
  echo "Warning: can't obtain nginx conf from '$NGINX_BIN -V'"
  NGINX_CONF_DIR=`dirname $NGINX_BIN`"/../conf"
fi

NGINX_CONF_DIR="${NGINX_CONF_DIR}/"

echo "Notice: Current config dir is in: $NGINX_CONF_DIR"

# Misc Errors 
if [ `id -u` != 0 ]; then 
 echo "Error: Please run as root";
 exit 0
fi

if [ ! -f  $NGINX_BIN ]; then
  echo "Error: $NGINX_BIN not found."
  exit 1;
fi

if [ ! -f  $NGINX_INIT ]; then
  echo "Error: $NGINX_INIT not found."
  exit 1;
fi

if [ ! -d $NGINX_CONF_DIR ]; then
  echo "Error: $NGINX_CONF_DIR not found."
  exit 1;
fi

if [ ! -f ${NGINX_CONF_DIR}nginx.conf ]; then
  echo "Error: ${NGINX_CONF_DIR}nginx.conf not found."
  exit 1;
fi

# Check default confs
if [ ! -d $NGINX_CONF_DIR$AUTO_DIR ]; then
  echo "Notice: Writing conf files to $NGINX_CONF_DIR$AUTO_DIR"
  mkdir $NGINX_CONF_DIR$AUTO_DIR 
  cp `dirname $0`/auto/* $NGINX_CONF_DIR$AUTO_DIR 
  chmod -R 755 $NGINX_CONF_DIR$AUTO_DIR
fi


# Check sites-available/enabled and logs
if [ ! -d $NGINX_CONF_DIR$S_AVAILABLE  ]; then
  echo "Notice: Creating $NGINX_CONF_DIR$S_AVAILABLE"
  mkdir $NGINX_CONF_DIR$S_AVAILABLE
  chmod -R 755 $NGINX_CONF_DIR$S_AVAILABLE
fi

if [ ! -d $NGINX_CONF_DIR$S_ENABLED  ]; then
  echo "Notice: Creating $NGINX_CONF_DIR$S_ENABLED"
  mkdir $NGINX_CONF_DIR$S_ENABLED
  chmod -R 755 $NGINX_CONF_DIR$S_ENABLED
fi

# Can't be sure where log dir is, disabling for now
#if [ ! -d $NGINX_CONF_DIR$LOGS_DIR ]; then
#  echo "Notice: Creating $NGINX_CONF_DIR$LOGS_DIR"
#  mkdir $NGINX_CONF_DIR$LOGS_DIR
#  chmod -R 777 $NGINX_CONF_DIR$LOGS_DIR
#fi


# Check params
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Not enough parameters"
  exit 0
else
  
  SERVERNAME="$1"
  DIRROOT="$2"
  
  if [ ! -d "$DIRROOT" ]; then
    echo "Error: $2 is not a directory"
    exit 0
  fi
  
  shift 2
  
fi 

# Options 
while [[ $1 = -* ]]; do
  case "$1" in
    -drupal)
      DRUPAL_CONF=1
      shift
      ;;
    -php)
      PHP_CONF=1
      shift
      ;;
    -cake)
      CAKE_CONF=1 
      shift
      ;;
    -mobile)
      MOBILE_CONF=1 
      shift
      ;;
    -magento)
      MAGENTO_CONF=1 
      shift
      ;;
    *)
      echo "Error: Invalid option: $1" >&2
      exit 1
      ;;
  esac
done

if [ ! "$DRUPAL_CONF" = 1 ] && [ ! "$PHP_CONF" = 1 ] && [ ! "$CAKE_CONF" = 1 ] && [ ! "$MOBILE_CONF" = 1 ] && [ ! "$MAGENTO_CONF" = 1 ]; then
  DEFAULT_CONF=1
fi 


# Creating files
if [ -e $NGINX_CONF_DIR$S_ENABLED$SERVERNAME ]; then
  rm  $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
fi

if [ ! -d "$NGINX_CONF_DIR$S_ENABLED" ] || [ ! -d "$NGINX_CONF_DIR$S_AVAILABLE" ]; then
  echo "Error: Not valid dirs $NGINX_CONF_DIR$S_ENABLED or $NGINX_CONF_DIR$S_AVAILABLE"
  exit 0
fi

# If php enabled, replace server config
if [ "$PHP_CONF" = 1 ]; then
  sed -i "" 's/fastcgi_pass\([^;]\)\+/fastcgi_pass  $PHPFM_SERVER:$PHPFM_PORT/g' $NGINX_CONF_DIR$AUTO_DIR/php.conf 
fi

# Desktop Version
echo "server {\n 
  listen *:$HTTP_PORT;
  server_name $SERVERNAME;
  root  $DIRROOT;

  access_log $LOGS_DIR$SERVERNAME.access.log;
  error_log $LOGS_DIR$SERVERNAME.error.log;\n
  
  location / {
      index  index.html index.htm index.php;
  }
  
  error_page   500 502 503 504  /50x.html;
  location = /50x.html {
      root   html;
  }\n" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME;
  

if [ "$MOBILE_CONF" = 1 ]; then

  echo "\n  if (\$http_user_agent ~* '(iPhone|iPod|Android|webOS)') {
    rewrite ^/\$ http://m.$SERVERNAME;
  }\n" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME

fi

if [ "$PHP_CONF" = 1 ]; then
  echo "  include  ${COMMON_DIR}php;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
fi

if [ "$CAKE_CONF" = 1 ]; then
  echo "  include ${COMMON_DIR}cake;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
fi

if [ "$DRUPAL_CONF" = 1 ]; then
  echo "  include ${COMMON_DIR}drupal;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
fi

if [ "$MAGENTO_CONF" = 1 ]; then
  echo "  include ${COMMON_DIR}magento;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
fi

if [ "$DEFAULT_CONF" = 1 ]; then
  echo "  include ${COMMON_DIR}default;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
fi
echo "\n}">> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME


# Mobile Version
if [ "$MOBILE_CONF" = 1 ]; then

  echo -e "\nserver {\n 
  listen *:$HTTP_PORT;
  index  index.html index.htm index.php;
  root  $DIRROOT;
  server_name m.$SERVERNAME;
  access_log $LOGS_DIRm.$SERVERNAME.access.log;
  error_log $LOGS_DIRm.$SERVERNAME.error.log;\n" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME

  if [ "$PHP_CONF" = 1 ]; then
    echo -e "  include ${COMMON_DIR}php;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
  fi

  if [ "$CAKE_CONF" = 1 ]; then
    echo -e "  include ${COMMON_DIR}cake;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
  fi

  if [ "$DRUPAL_CONF" = 1 ]; then
    echo -e "  include ${COMMON_DIR}drupal;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
  fi
  
  if [ "$MAGENTO_CONF" = 1 ]; then
    echo -e "  include ${COMMON_DIR}magento;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
  fi

  if [ "$DEFAULT_CONF" = 1 ]; then
    echo -e "   include ${COMMON_DIR}default;" >> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
  fi
  
  echo -e "\n}">> $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME
  
fi

# Cleaning an creating new link and restarting
if [ -e $NGINX_CONF_DIR$S_ENABLED$SERVERNAME ]; then
  rm $NGINX_CONF_DIR$S_ENABLED$SERVERNAME
fi
ln -s $NGINX_CONF_DIR$S_AVAILABLE$SERVERNAME $NGINX_CONF_DIR$S_ENABLED$SERVERNAME
$RESTART_CMD

echo "Done!"
exit 0



