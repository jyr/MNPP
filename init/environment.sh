#!/bin/sh

__export_library( ){
	touch /Users/$SUDO_USER/.bash_profile
	found=`cat /Users/$SUDO_USER/.bash_profile | grep MNPP | wc -l`
	export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/lib:$DYLD_LIBRARY_PATH
 	NGINX_LOGS='/Applications/MNPP/Library/nginx/logs'
	
	if [ ! -d $NGINX_LOGS ]; then
		mkdir $NGINX_LOGS
	fi

  if [ $found = 0 ] ; then
		echo "alias drush='/Applications/MNPP/Library/bin/php /Applications/MNPP/Library/drush/drush.php'" >> /Users/$SUDO_USER/.bash_profile
		echo "export PATH=/Applications/MNPP/init:/Applications/MNPP/Library/php54/bin:/Applications/MNPP/Library/mysql/bin:\$PATH" >> /Users/$SUDO_USER/.bash_profile
		echo "alias mysql='/Applications/MNPP/Library/mysql/bin/mysql --socket=/Applications/MNPP/tmp/mysql/mysql.sock'" >> /Users/$SUDO_USER/.bash_profile
		echo "export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/lib:$DYLD_LIBRARY_PATH" >> /Users/$SUDO_USER/.bash_profile
  fi
}

__export_library
