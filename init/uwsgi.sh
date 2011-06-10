#!/bin/sh
NAME=uwsgi

DYLD_LIBRARY_PATH=/Applications/MNPP/Library/lib:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH
launchctl setenv DYLD_LIBRARY_PATH $DYLD_LIBRARY_PATH

case "$1" in
  start)
        echo "Starting $NAME: "
        
        launchctl load /Applications/MNPP/Library/LaunchAgents/it.unbit.uwsgi.plist 
        launchctl start it.unbit.uwsgi
        
        echo "Done."
        ;;
  stop)
        echo "Stopping $NAME: "
        
        launchctl stop it.unbit.uwsgi 
        launchctl unload /Applications/MNPP/Library/LaunchAgents/it.unbit.uwsgi.plist 
        
        echo "Done."
        ;;
      *)  
            N=/Applications/MNPP/init/$NAME.sh
            echo "Usage: $N {start|stop}" >&2
            exit 1
            ;;
    esac
    exit 0
