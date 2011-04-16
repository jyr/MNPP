Percona
---

rm sql/sql_yacc.h    
rm sql/sql_yacc.cc    
BUILD/autorun.sh    

CFLAGS="-arch i386 -arch x86_64 -O3 -fno-omit-frame-pointer" CXXFLAGS="-arch i386 -arch x86_64 -O3 -fno-omit-frame-pointer -felide-constructors -fno-exceptions -fno-rtti" ./configure --prefix=/Applications/MNPP/Library/mysql --disable-dependency-tracking --with-extra-charsets=complex --enable-thread-safe-client --enable-local-infile --with-unix-socket-path=/Applications/MNPP/tmp/mysql/mysql.sock --with-charset=latin1 --with-collation=latin1_general_ci --with-mysqld-user=_mysql --enable-shared --with-plugins=all    

make    
make install

Freetype
---
./configure --prefix=/Applications/MNPP/Library/freetype    
make    
make install

Curl
----
./configure --prefix=/Applications/MNPP/Library/curl    
make    
make install

JPEG
---
./configure --prefix=/Applications/MNPP/Library/jpeg    
make    
make install

Libpng
---
./configure --prefix=/Applications/MNPP/Library/libpng    
make    
make install

GD
---
./configure --prefix=/Applications/MNPP/Library/gd    
make    
make install

LibXML
---
./configure --prefix=/Applications/MNPP/Library/libxml    
make    
make install

LibXSLT
---
./configure --prefix=/Applications/MNPP/Library/libxslt    
make    
make install

Gettext
---
./configure --prefix=/Applications/MNPP/Library/gettext    
make    
make install

LibMCRYPT
---
./configure --prefix=/Applications/MNPP/Library/mcrypt    
make    
make install

MCRYPT
---
./configure --prefix=/Applications/MNPP/Library/mcrypt    
make    
make install

Libiconv
---
./configure --prefix=/Applications/MNPP/Library/libiconv    
make    
make install

PDO_MYSQL
---
cd PDO_MYSQL-1.0.2/    
phpize    
./configure --with-pdo-mysql=shared,/Applications/MNPP/Library/mysql/    
make    
cp modules/pdo_mysql.so /Applications/MNPP/Library/php/lib/php/extensions/no-debug-non-zts-20090626/

Libevent
---
./configure --prefix=/Applications/MNPP/Library/libevent    
make    
make install

MEMCACHED
---
./configure --prefix=/Applications/MNPP/Library/memcached --with-libevent=/Applications/MNPP/Library/libevent/    
make    
make install

PHP-MEMCACHE http://pecl.php.net/package/memcache 
cd memcache-3.0.5   
phpize && ./configure --enable-memcache && make    
cp modules/memcache.so /Applications/MNPP/Library/php/lib/php/extensions/no-debug-non-zts-20090626    
add extension=memcache.so in php.ini

APC
---
APC http://pecl.php.net/package/APC    
phpize    

MACOSX_DEPLOYMENT_TARGET=10.6 CFLAGS="-arch x86_64 -g -Os -pipe -no-cpp-precomp" CCFLAGS="-arch x86_64 -g -Os -pipe" CXXFLAGS="-arch x86_64 -g -Os -pipe" LDFLAGS="-arch x86_64 -bind_at_load" ./configure --with-php-config=/Applications/MNPP/Library/php/bin/php-config    
make    
cp modules/apc.so /Applications/MNPP/Library/php/lib/php/extensions/no-debug-non-zts-20090626    
add extension=memcache.so in php.ini    

MONGO
---
https://github.com/mongodb/mongo-php-driver    
cd mongodb-mongo-php-driver-*    
./configure    
sudo make install    
cp modules/mongo.so /Applications/MNPP/Library/php/lib/php/extensions/no-debug-non-zts-20090626/    
add extension=mongo.so in php.ini    

PHP
---
./configure --prefix=/Applications/MNPP/Library/php --exec-prefix=/Applications/MNPP/Library/php --enable-cli --enable-gd-jis-conv --enable-gd-native-ttf --enable-mbstring --with-bz2 --with-curl=/Applications/MNPP/Library/curl --with-gd=/Applications/MNPP/Library/gd --with-gettext=shared,/Applications/MNPP/Library/gettext --with-freetype-dir=/Applications/MNPP/Library/freetype --with-jpeg-dir=/Applications/MNPP/Library/jpeg --with-libxml-dir=/Applications/MNPP/Library/libxml --with-xsl=/Applications/MNPP/Library/libxslt --with-mcrypt=shared,/Applications/MNPP/Library/mcrypt --with-mhash --with-mysql=/Applications/MNPP/Library/mysql --enable-sockets --with-mysqli=/Applications/MNPP/Library/mysql/bin/mysql_config  --with-openssl --with-png-dir=/Applications/MNPP/Library/libpng --with-readline --with-xpm-dir=/Applications/MNPP/Library/xpm --with-zlib --with-config-file-path=/Applications/MNPP/conf/php5 --enable-fpm --with-fpm-user=www-data --with-fpm-group=www-data --with-libedit --enable-libxml --enable-dom --enable-simplexml --with-iconv=/Applications/MNPP/Library/libiconv --with-pdo-mysql=/Applications/MNPP/Library/mysql/bin/mysql_config    
make    
make install    

NGINX
---
./configure --prefix=/Applications/MNPP/Library/nginx --sbin-path=/Applications/MNPP/Library/nginx --conf-path=/Applications/MNPP/conf/nginx/nginx.conf --user=www --group=www --with-http_ssl_module --with-http_stub_status_module --pid-path=/Applications/MNPP/run/nginx --with-http_gzip_static_module --with-pcre=/Applications/MNPP/src/pcre-8.11/    
make    
make install