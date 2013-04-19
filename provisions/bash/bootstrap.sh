#!/bin/sh

export DYLD_LIBRARY_PATH=/Applications/MNPP/init:/Applications/MNPP/Library/lib:$DYLD_LIBRARY_PATH

__initialize( ){
	
	# Requeriments - Xcode and Command Line Tools
	# from https://developer.apple.com/downloads/index.action

	SRC='/Applications/MNPP/src'
	LIBS='/Applications/MNPP/Library/lib'

	if [ ! -d $SRC ]; then
		mkdir $SRC
		__essentials
	fi
	
	if [ ! -d $LIBS ]; then
		mkdir $LIBS
	fi

	cd $SRC
	
	__sources
	__dependencies
}

__sources( ){

	# Percona Source
	#

	PERCONA_URL='http://www.percona.com/redir/downloads/Percona-Server-5.5/Percona-Server-5.5.30-30.2/source/'
	PERCONA_FILE='Percona-Server-5.5.30-rel30.2'

	# PHP Libs
	#

	JPEG_URL='http://www.ijg.org/files/'
	JPEG_FILE='jpegsrc.v9'
	JPEG_VERSION='9'
	JPEG_FLAGS=""
	JPEG_SOURCE="jpeg-${JPEG_VERSION}"
	JPEG_OPTIONS="--enable-shared --enable-static"

	PNG_URL='http://downloads.sourceforge.net/project/libpng/libpng16/1.6.1/'
	PNG_FILE='libpng-1.6.1'
	PNG_VERSION='1.6.1'
	PNG_FLAGS=""
	PNG_SOURCE="${PNG_FILE}"
	PNG_OPTIONS=""

	XPM_URL='http://xorg.freedesktop.org/releases/individual/lib/'
	XPM_FILE='libXpm-3.5.10'
	XPM_VERSION='3.5.10'
	XPM_FLAGS=""
	XPM_SOURCE="${XPM_FILE}"
	XPM_OPTIONS=""

	FREETYPE_URL='http://downloads.sourceforge.net/project/freetype/freetype2/2.4.11/'
	FREETYPE_FILE='freetype-2.4.11'
	FREETYPE_VERSION='2.4.11'
	FREETYPE_FLAGS=""
	FREETYPE_SOURCE="${FREETYPE_FILE}"
	FREETPE_OPTIONS=""

	GETTEXT_URL='http://ftp.gnu.org/pub/gnu/gettext/'
	GETTEXT_FILE='gettext-0.18.2'
	GETTEXT_VERSION='0.18.2'
	GETTEXT_FLAGS=`CFLAGS="-arch i386 -arch x86_64" CXXFLAGS="-arch i386 -arch x86_64"`
	GETTEXT_SOURCE="${GETTEXT_FILE}"
	GETTEXT_OPTIONS="--with-libiconv-prefix=/Applications/MNPP/Library/iconv/"


	LIBMCRYPT_URL='http://downloads.sourceforge.net/project/mcrypt/Libmcrypt/2.5.8/'
	LIBMCRYPT_FILE='libmcrypt-2.5.8'
	LIBMCRYPT_VERSION='2.5.8'
	LIBMCRYPT_FLAGS=""
	LIBMCRYPT_SOURCE="${LIBMCRYPT_FILE}"
	LIBMCRYPT_OPTIONS=""

	MCRYPT_URL='http://downloads.sourceforge.net/project/mcrypt/MCrypt/2.6.8/'
	MCRYPT_FILE='mcrypt-2.6.8'
	MCRYPT_VERSION='2.6.8'
	MCRYPT_FLAGS=""
	MCRYPT_SOURCE="${MCRYPT_FILE}"
	MCRYPT_OPTIONS=""


	XML_URL='ftp://xmlsoft.org/libxml2/'
	XML_FILE='libxml2-2.8.0'
	XML_VERSION='2.8.0'
	XML_FLAGS=""
	XML_SOURCE="${XML_FILE}"
	XML_OPTIONS=""

	XSLT_URL='http://xmlsoft.org/sources/'
	XSLT_FILE='libxslt-1.1.28'
	XSLT_VERSION='1.1.28'
	XSLT_FLAGS=""
	XSLT_SOURCE="${XSLT_FILE}"
	XSLT_OPTIONS=""

	ICONV_URL='http://ftp.gnu.org/pub/gnu/libiconv/'
	ICONV_FILE='libiconv-1.14'
	ICONV_VERSION='1.14'
	ICONV_FLAGS=""
	ICONV_SOURCE="${ICONV_FILE}"
	ICONV_OPTIONS=""

	MHASH_URL='http://downloads.sourceforge.net/project/mhash/mhash/0.9.9.9/'
	MHASH_FILE='mhash-0.9.9.9'
	MHASH_VERSION='0.9.9.9'
	MHASH_FLAGS=""
	MHASH_SOURCE="${MHASH_FILE}"
	MHASH_OPTIONS=""

	GD_URL='http://download.osgeo.org/mapserver/libgd/'
	GD_FILE='gd-2.0.36RC1'
	GD_VERSION='2.0.36RC1'
	GD_FLAGS=""
	GD_SOURCE="${GD_FILE}"
	GD_OPTIONS=""

	PCRE_URL='http://downloads.sourceforge.net/project/pcre/pcre/8.32/'
	PCRE_FILE='pcre-8.32'

	NGINX_URL="http://nginx.org/download/"
	NGINX_FILE="nginx-1.2.8"

	# PHP Versions
	#

	PHP54_URL='http://us2.php.net/get/php-5.4.13.tar.gz/from/this/mirror'
	PHP54_FILE='php54-src'
	PHP54_VERSION='5.4.13'
	
	PHP53_URL='http://us2.php.net/get/php-5.3.24.tar.gz/from/this/mirror'
	PHP53_FILE='php53-src'
	PHP53_VERSION='5.3.24'
	
	PHP52_URL='http://museum.php.net/php5/'
	PHP52_FILE='php52-src'
	PHP52_VERSION='5.2.17'
}

__essentials( ){
	brew install cmake libtool pkg-config curl openssl
}

__nginx( ) {
	wget -c "${PCRE_URL}${PCRE_FILE}.tar.gz"  && tar xvfz "${PCRE_FILE}.tar.gz"
	wget -c  "${NGINX_URL}${NGINX_FILE}.tar.gz" && tar zxvf "${NGINX_FILE}.tar.gz" && cd "${NGINX_FILE}"

	./configure --prefix=/Applications/MNPP/Library/nginx --sbin-path=/Applications/MNPP/Library/nginx --conf-path=/Applications/MNPP/conf/nginx/nginx.conf --user=www --group=www --with-http_ssl_module --with-http_stub_status_module --pid-path=/Applications/MNPP/run/nginx --with-http_gzip_static_module --with-pcre=/Applications/MNPP/src/$PCRE_FILE/

	make && make install
}

__percona( ){

	wget -c "${PERCONA_URL}${PERCONA_FILE}.tar.gz"
	tar -zxvf "${PERCONA_FILE}.tar.gz"
	cd $PERCONA_FILE
	BUILD/autorun.sh

	CFLAGS="-arch i386 -arch x86_64 -O3 -fno-omit-frame-pointer" CXXFLAGS="-arch i386 -arch x86_64 -O3 -fno-omit-frame-pointer -felide-constructors -fno-exceptions -fno-rtti" ./configure --prefix=/Applications/MNPP/Library/mysql --disable-dependency-tracking --with-extra-charsets=complex --enable-thread-safe-client --enable-local-infile --with-unix-socket-path=/Applications/MNPP/tmp/mysql/mysql.sock --with-charset=latin1 --with-collation=latin1_general_ci --with-mysqld-user=_mysql --enable-shared --with-plugins=all --datadir=/Applications/MNPP/Library/mysql/var/

	make && make install
	
	mkdir /Applications/MNPP/Library/mysql/var
	wget -c -O /Applications/MNPP/Library/mysql/my.cnf https://gist.github.com/jyr/5418650/raw/d6ea07a725aff419caaa1e3fcb5471cc3dff1a05/my.cnf
	chown -R mysql:mysql /Applications/MNPP/Library/mysql

	sh /Applications/MNPP/src/$PERCONA_FILE/scripts/mysql_install_db.sh --user=mysql --ldata=/Applications/MNPP/Library/mysql/var/ --basedir=/Applications/MNPP/Library/mysql/
	cp /Applications/MNPP/Library/mysql/lib/libmysqlclient.18.dylib /Applications/MNPP/Library/lib/
}

__php( ){
	__php_54
	__php_53
	__php_52
}
__php_54( ){

	### PHP VERSION 5.4.*

	wget -c -O "${PHP54_FILE}.tar.gz" "${PHP54_URL}"
	echo "${PHP54_FILE}.tar.gz ${PHP54_URL}"
	tar xvfz "${PHP54_FILE}.tar.gz" && cd "php-${PHP54_VERSION}"

	./configure --prefix=/Applications/MNPP/Library/php54 --exec-prefix=/Applications/MNPP/Library/php54 --enable-cli --enable-gd-jis-conv --enable-gd-native-ttf --enable-mbstring --with-bz2 --with-curl --with-gd --with-gettext=shared,/Applications/MNPP/Library/gettext --with-freetype-dir=/Applications/MNPP/Library/freetype --with-jpeg-dir=/Applications/MNPP/Library/jpeg --with-libxml-dir=/Applications/MNPP/Library/xml --with-xsl=/Applications/MNPP/Library/xslt --with-mcrypt=shared,/Applications/MNPP/Library/mcrypt --with-mhash=/Applications/MNPP/Library/mhash --with-mysql=/Applications/MNPP/Library/mysql --enable-sockets --with-mysqli=/Applications/MNPP/Library/mysql/bin/mysql_config --with-openssl-dir=/usr/include/openssl --with-zlib-dir=/Applications/MNPP/Library/zlib --with-png-dir=/Applications/MNPP/Library/png --with-readline --with-zlib --with-config-file-path=/Applications/MNPP/conf/php54 --enable-fpm --with-fpm-user=www --with-fpm-group=www --with-libedit --enable-libxml --enable-dom --enable-simplexml --with-iconv=/Applications/MNPP/Library/iconv --with-pdo-mysql=/Applications/MNPP/Library/mysql/bin/mysql_config --enable-soap

	export EXTRA_CFLAGS=-lresolv
	export LC_ALL=en_US.UTF-8
	make && make install
}

__php_53( ) {

	### PHP VERSION 5.3.*

	wget -c -O "${PHP53_FILE}.tar.gz" "${PHP53_URL}"
	tar xvfz "${PHP53_FILE}.tar.gz" && cd "php-${PHP53_VERSION}"

	./configure --prefix=/Applications/MNPP/Library/php53 --exec-prefix=/Applications/MNPP/Library/php53 --enable-cli --enable-gd-jis-conv --enable-gd-native-ttf --enable-mbstring --with-bz2 --with-curl --with-gd=/Applications/MNPP/Library/gd --with-gettext=shared,/Applications/MNPP/Library/gettext --with-freetype-dir=/Applications/MNPP/Library/freetype --with-jpeg-dir=/Applications/MNPP/Library/jpeg --with-libxml-dir=/Applications/MNPP/Library/xml --with-xsl=/Applications/MNPP/Library/xslt --with-mcrypt=shared,/Applications/MNPP/Library/mcrypt --with-mhash=/Applications/MNPP/Library/mhash --with-mysql=/Applications/MNPP/Library/mysql --enable-sockets --with-mysqli=/Applications/MNPP/Library/mysql/bin/mysql_config --with-openssl-dir=/usr/include/openssl --with-zlib-dir=/Applications/MNPP/Library/zlib --with-png-dir=/Applications/MNPP/Library/png --with-readline --with-zlib --with-config-file-path=/Applications/MNPP/conf/php53 --enable-fpm --with-fpm-user=www --with-fpm-group=www --with-libedit --enable-libxml --enable-dom --enable-simplexml --with-iconv=/Applications/MNPP/Library/iconv --with-pdo-mysql=/Applications/MNPP/Library/mysql/bin/mysql_config --enable-soap

	export EXTRA_CFLAGS=-lresolv
	make && make install
}

__php_52( ) {

	### PHP VERSION 5.2.*

	wget -c -O "${PHP52_FILE}.tar.gz" "${PHP52_URL}""php-${PHP52_VERSION}.tar.gz"
	tar xvfz "${PHP52_FILE}.tar.gz" && cd "php-${PHP52_VERSION}"
	wget -c http://php-fpm.org/downloads/php-5.2.17-fpm-0.5.14.diff.gz
	gunzip php-5.2.17-fpm-0.5.14.diff.gz
	patch -p1 < php-5.2.17-fpm-0.5.14.diff

	./configure --prefix=/Applications/MNPP/Library/php52 --exec-prefix=/Applications/MNPP/Library/php52 --enable-cli --enable-gd-jis-conv --enable-gd-native-ttf --enable-mbstring --with-bz2 --with-curl=/Applications/MNPP/Library/curl --with-gd=/Applications/MNPP/Library/gd --with-gettext=shared,/Applications/MNPP/Library/gettext --with-freetype-dir=/Applications/MNPP/Library/freetype --with-jpeg-dir=/Applications/MNPP/Library/jpeg --with-libxml-dir=/Applications/MNPP/Library/xml --with-xsl=/Applications/MNPP/Library/xslt --with-mcrypt=shared,/Applications/MNPP/Library/mcrypt --with-mhash=/Applications/MNPP/Library/mhash --with-mysql=/Applications/MNPP/Library/mysql --enable-sockets --with-mysqli=/Applications/MNPP/Library/mysql/bin/mysql_config --with-openssl-dir=/usr/include/openssl --with-png-dir=/Applications/MNPP/Library/png --with-readline --with-ttf --with-zlib --with-config-file-path=/Applications/MNPP/conf/php52 --enable-fastcgi --enable-fpm --enable-force-cgi-redirect --with-fpm-conf=/Applications/MNPP/conf/php52/php-fpm --with-fpm-log=/Applications/MNPP/logs/php52/php-fpm.log --with-fpm-pid=/Applications/MNPP/tmp/php52/php-fpm.pid --with-libedit --enable-libxml --enable-dom --with-ncurses=/usr/lib --enable-pdo --with-pcre-regex --enable-hash --enable-session --enable-json --enable-spl --enable-filter --enable-simplexml --enable-xml --with-iconv=/Applications/MNPP/Library/iconv --enable-soap

	make && make install

}

__compile_libs( ) {
	LIB_NAME="${1}"
	FILE="${2}"
	URL="${3}"
	VERSION="${4}"
	SOURCE="${5}"
	OPTIONS="${6}"
	FLAGS="${7}"
	
	wget -c -O "${SOURCE}.tar.gz" "${URL}${FILE}.tar.gz"
	tar -zxvf "${SOURCE}.tar.gz" && cd "${SOURCE}"
	$FLAGS ./configure --prefix=/Applications/MNPP/Library/$LIB_NAME $OPTIONS
	make &&	make install
}

__jpeg( ) {
	__compile_libs "jpeg" $JPEG_FILE $JPEG_URL $JPEG_VERSION $JPEG_SOURCE "${JPEG_OPTIONS}" $JPEG_FLAGS
}

__png( ) {
	__compile_libs "png" $PNG_FILE $PNG_URL $PNG_VERSION $PNG_SOURCE $PNG_OPTIONS $PNG_FLAGS
}

__freetype( ) {
	__compile_libs "freetype" $FREETYPE_FILE $FREETYPE_URL $FREETYPE_VERSION $FREETYPE_SOURCE $FREETYPE_OPTIONS $FREETYPE_FLAGS
}

__gettext( ) {
	__compile_libs "gettext" $GETTEXT_FILE $GETTEXT_URL $GETTEXT_VERSION $GETTEXT_SOURCE "${GETTEXT_OPTIONS}" $GETTEXT_FLAGS
}

__libmcrypt( ) {
	__compile_libs "mcrypt" $LIBMCRYPT_FILE $LIBMCRYPT_URL $LIBMCRYPT_VERSION $LIBMCRYPT_SOURCE "${LIBMCRYPT_OPTIONS}" $LIBMCRYPT_FLAGS
}

__mcrypt( ) {
	__compile_libs "mcrypt" $MCRYPT_FILE $MCRYPT_URL $MCRYPT_VERSION $MCRYPT_SOURCE "${MCRYPT_OPTIONS}" $MCRYPT_FLAGS
}

__xml( ) {
	__compile_libs "xml" $XML_FILE $XML_URL $XML_VERSION $XML_SOURCE "${XML_OPTIONS}" $XML_FLAGS
}

__xslt( ) {
	__compile_libs "xslt" $XSLT_FILE $XML_URL $XSLT_VERSION $XSLT_SOURCE "${XSLT_OPTIONS}" $XSLT_FLAGS
}

__iconv( ) {
	__compile_libs "iconv" $ICONV_FILE $ICONV_URL $ICONV_VERSION $ICONV_SOURCE "${ICONV_OPTIONS}" $ICONV_FLAGS
}

__mhash( ) {
	__compile_libs "mhash" $MHASH_FILE $MHASH_URL $MHASH_VERSION $MHASH_SOURCE "${MHASH_OPTIONS}" $MHASH_FLAGS
}

__gd( ) {
	__compile_libs "gd" $GD_FILE $GD_URL $GD_VERSION $GD_SOURCE "${GD_OPTIONS}" $GD_FLAGS
}

__dependencies( ){
	__jpeg
	__png
	__freetype
	__gettext
	__libmcrypt
	__mcrypt
	__xml
	__xslt
	__iconv
	__mhash
	__gd
}

__reset( ){
	chown -R $SUDO_USER /Applications/MNPP/Library
	chown -R mysql:mysql /Applications/MNPP/Library/mysql
}

__initialize
__nginx
__percona
__php
__reset
