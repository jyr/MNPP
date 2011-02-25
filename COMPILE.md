Percona
---

rm sql/sql_yacc.h
rm sql/sql_yacc.cc
BUILD/autorun.sh

CFLAGS="-arch i386 -arch x86_64 -O3 -fno-omit-frame-pointer" CXXFLAGS="-arch i386 -arch x86_64 -O3 -fno-omit-frame-pointer -felide-constructors -fno-exceptions -fno-rtti" ./configure --prefix=/Applications/MEPP/Library/mysql --disable-dependency-tracking --with-extra-charsets=complex --enable-thread-safe-client --enable-local-infile --with-unix-socket-path=/Applications/MEPP/tmp/mysql/mysql.sock --with-charset=latin1 --with-collation=latin1_general_ci --with-mysqld-user=_mysql --enable-shared --with-plugins=all

make
make install

Freetype
---
./configure --prefix=/Applications/MEPP/Library/freetype
make
make install

Curl
----
./configure --prefix=/Applications/MEPP/Library/curl
make
make install

JPEG
---
./configure --prefix=/Applications/MEPP/Library/jpeg
make
make install

Libpng
---
./configure --prefix=/Applications/MEPP/Library/libpng
make
make install

GD
---
./configure --prefix=/Applications/MEPP/Library/gd
make
make install

LibXML
---
./configure --prefix=/Applications/MEPP/Library/libxml
make
make install

LibXSLT
---
./configure --prefix=/Applications/MEPP/Library/libxslt
make
make install

Gettext
---
./configure --prefix=/Applications/MEPP/Library/gettext
make 
make install

LibMCRYPT
---
./configure --prefix=/Applications/MEPP/Library/mcrypt
make
make install

MCRYPT
---
./configure --prefix=/Applications/MEPP/Library/mcrypt
make
make install

Libiconv
---
./configure --prefix=/Applications/MEPP/Library/libiconv
make
make install

PDO_MYSQL
cd PDO_MYSQL-1.0.2/
phpize
./configure --with-pdo-mysql=shared,/Applications/MEPP/Library/mysql/
make
cp modules/pdo_mysql.so /Applications/MEPP/Library/php/lib/php/extensions/no-debug-non-zts-20090626/



PHP
---
./configure --prefix=/Applications/MEPP/Library/php --exec-prefix=/Applications/MEPP/Library/php --enable-cli --enable-gd-jis-conv --enable-gd-native-ttf --enable-mbstring --with-bz2 --with-curl=/Applications/MEPP/Library/curl --with-gd=/Applications/MEPP/Library/gd --with-gettext=shared,/Applications/MEPP/Library/gettext --with-freetype-dir=/Applications/MEPP/Library/freetype --with-jpeg-dir=/Applications/MEPP/Library/jpeg --with-libxml-dir=/Applications/MEPP/Library/libxml --with-xsl=/Applications/MEPP/Library/libxslt --with-mcrypt=shared,/Applications/MEPP/Library/mcrypt --with-mhash --with-mysql=/Applications/MEPP/Library/mysql --enable-sockets --with-mysqli=/Applications/MEPP/Library/mysql/bin/mysql_config  --with-openssl --with-png-dir=/Applications/MEPP/Library/libpng --with-readline --with-xpm-dir=/Applications/MEPP/Library/xpm --with-zlib --with-config-file-path=/Applications/MEPP/conf/php5 --enable-fpm --with-fpm-user=www-data --with-fpm-group=www-data --with-libedit --enable-libxml --enable-dom --enable-simplexml --with-iconv=/Applications/MEPP/Library/libiconv --with-pdo-mysql=/Applications/MEPP/Library/mysql/bin/mysql_config --with-mcrypt-dir=/Applications/MEPP/Library/mcrypt
make 
make install

NGINX
---
./configure --prefix=/Applications/MEPP/Library/nginx --sbin-path=/Applications/MEPP/Library/nginx --conf-path=/Applications/MEPP/conf/nginx/nginx.conf --user=www --group=www --with-http_ssl_module --with-http_stub_status_module --pid-path=/Applications/MEPP/run/nginx --with-http_gzip_static_module --with-pcre=/Applications/MEPP/src/pcre-8.11/
make
make install