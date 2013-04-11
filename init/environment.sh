#!/bin/sh

__export_library( ){
	touch /Users/$SUDO_USER/.bash_profile
	found=`cat /Users/$SUDO_USER/.bash_profile | grep MNPP | wc -l`
	export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/$OS_VERSION:$DYLD_LIBRARY_PATH
  ln -s /Applications/MNPP/Library/10.7/mysql/lib/libmysqlclient.18.dylib /usr/lib/
  
  	if [ $found = 0 ] ; then
		echo "alias drush='/Applications/MNPP/Library/php53/bin/php /Applications/MNPP/Library/$OS_VERSION/drush/drush.php'" >> /Users/$SUDO_USER/.bash_profile
		echo "export PATH=/Applications/MNPP/init:/Applications/MNPP/Library/$OS_VERSION/php53/bin:/Applications/MNPP/Library/$OS_VERSION/mysql/bin:\$PATH" >> /Users/$SUDO_USER/.bash_profile
		echo "alias mysql='/Applications/MNPP/Library/$OS_VERSION/mysql/bin/mysql --socket=/Applications/MNPP/tmp/mysql/mysql.sock'" >> /Users/$SUDO_USER/.bash_profile
		echo "export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/$OS_VERSION:$DYLD_LIBRARY_PATH" >> /Users/$SUDO_USER/.bash_profile
  	fi
}

__export_library
