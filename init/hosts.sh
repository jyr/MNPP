#! /bin/bash
# Fork of http://www.clauswitt.com/319/

DEFAULT_IP=127.0.0.1
IP=${3:-$DEFAULT_IP}

function add {
  found=`cat /etc/hosts | grep "$IP $2" | wc -l`

  if [ $found = 0 ] ; then
    echo "$IP $2"  >> /etc/hosts
  fi
}

function del {
  sed -ie "\|^$IP $2\$|d" /etc/hosts
}

function usage {
  echo "Usage: "
          echo "hosts.sh [add|del] [hostname] [ip]"
          echo
          echo "Ip defaults to 127.0.0.1"
          echo "Examples:"
          echo "hosts.sh --add drupal.local"
          echo "hosts.sh --del drupal.local 192.168.1.1"
  exit 1
}

case "$1" in
  --add)
        add $IP $2
        ;;
  --del)
        del $IP $2
        ;;

  *)
        usage
        ;;
esac

exit 0
