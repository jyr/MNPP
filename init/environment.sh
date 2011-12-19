#!/bin/sh

__export_library( ){
	touch /Users/$USER/.bash_profile
	found=`cat /Users/$USER/.bash_profile | grep "$IP $2" | wc -l`

  	if [ $found = 0 ] ; then
		echo "alias drush='/Applications/MNPP/Library/php53/bin/php /Applications/MNPP/Library/drush/drush.php'" >> /Users/$USER/.bash_profile
		echo "export PATH=/Applications/MNPP/init:/Applications/MNPP/Library/php53/bin:/Applications/MNPP/Library/mysql/bin:\$PATH" >> /Users/$USER/.bash_profile
		echo "export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/lib:\$DYLD_LIBRARY_PATH" >> /Users/$USER/.bash_profile
  	fi
}

__export_library