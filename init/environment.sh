#!/bin/sh

__export_library( ){
	touch /Users/$SUDO_USER/.bash_profile
	touch /var/$USER/.bash_profile
	found=`cat /Users/$SUDO_USER/.bash_profile | grep MNPP | wc -l`
	export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/$OS_VERSION/lib:$DYLD_LIBRARY_PATH
	OS_VERSION=`sw_vers -productVersion | grep -o 10\..`
	export OS_VERSION
  
  	if [ $found = 0 ] ; then
		echo $USER
		echo "OS_VERSION=`sw_vers -productVersion | grep -o 10\..`" >> /var/$USER/.bash_profile
		echo "export OS_VERSION" >> /var/$USER/.bash_profile
		echo "alias drush='/Applications/MNPP/Library/$OS_VERSION/bin/php /Applications/MNPP/Library/$OS_VERSION/drush/drush.php'" >> /Users/$SUDO_USER/.bash_profile
		echo "export PATH=/Applications/MNPP/init:/Applications/MNPP/Library/$OS_VERSION/php53/bin:/Applications/MNPP/Library/$OS_VERSION/mysql/bin:\$PATH" >> /Users/$SUDO_USER/.bash_profile
		echo "alias mysql='/Applications/MNPP/Library/$OS_VERSION/mysql/bin/mysql --socket=/Applications/MNPP/tmp/mysql/mysql.sock'" >> /Users/$SUDO_USER/.bash_profile
		echo "export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/$OS_VERSION:$DYLD_LIBRARY_PATH" >> /Users/$SUDO_USER/.bash_profile
		mkdir /Applications/MNPP/Library/$OS_VERSION/nginx/logs
  	fi
}

__export_library
