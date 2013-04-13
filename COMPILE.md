First run
---

OS_VERSION=`sw_vers -productVersion | grep -o 10\..`
export OS_VERSION

Percona
---
   
BUILD/autorun.sh    

CFLAGS="-arch i386 -arch x86_64 -O3 -fno-omit-frame-pointer" CXXFLAGS="-arch i386 -arch x86_64 -O3 -fno-omit-frame-pointer -felide-constructors -fno-exceptions -fno-rtti" ./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/mysql --disable-dependency-tracking --with-extra-charsets=complex --enable-thread-safe-client --enable-local-infile --with-unix-socket-path=/Applications/MNPP/tmp/mysql/mysql.sock --with-charset=latin1 --with-collation=latin1_general_ci --with-mysqld-user=_mysql --enable-shared --with-plugins=all --datadir=/Applications/MNPP/Library/$OS_VERSION/mysql/var/

make && make install    
sudo mkdir /Applications/MNPP/Library/$OS_VERSION/mysql/var; chown -R mysql:mysql /Applications/MNPP/Library/$OS_VERSION/mysql/var    
sudo sh src/Percona-Server-5.5.30-rel30.1/scripts/mysql_install_db.sh --user=mysql --ldata=/Applications/MNPP/Library/$OS_VERSION/mysql/var/ --basedir=/Applications/MNPP/Library/$OS_VERSION/mysql/

Freetype
---
wget -c http://downloads.sourceforge.net/project/freetype/freetype2/2.4.11/freetype-2.4.11.tar.bz2    
tar -jxvf freetype-2.4.11.tar.bz2   
./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/freetype    
make    
make install

Curl
----
./configure --prefix=/Applications/MNPP/Library/curl    
make    
make install

JPEG
---
wget -c http://www.ijg.org/files/jpegsrc.v9.tar.gz
tar -zxvf jpegsrc.v9.tar.gz    
./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/jpeg --enable-shared --enable-static    
make    
make install

Libpng
---
wget -c http://downloads.sourceforge.net/project/libpng/libpng16/1.6.1/libpng-1.6.1.tar.gz    
./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/libpng    
make && make install    

GD
---

#MACOSX_DEPLOYMENT_TARGET=10.7 CFLAGS="-arch x86_64 -g -Os -pipe -no-cpp-precomp" CCFLAGS="-arch x86_64 -g -Os -pipe" CXXFLAGS="-arch x86_64 -g -Os -pipe" LDFLAGS="-arch x86_64 -bind_at_load" ./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/gd --with-jpeg=/Applications/MNPP/Library/$OS_VERSION/jpeg
https://bitbucket.org/pierrejoye/gd-libgd/get/197ed9ab8a12.zip
unzip pierrejoye-gd-libgd-197ed9ab8a12.zip
cd pierrejoye-gd-libgd-197ed9ab8a12
mkdir build
cd build 
cmake -DCMAKE_INSTALL_PREFIX:PATH=/Applications/MNPP/Library/$OS_VERSION/gd ..
make && make install

LibXML
---
wget -c ftp://xmlsoft.org/libxml2/libxml2-2.8.0.tar.gz    
./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/libxml    
make    
make install

LibXSLT
---
./configure --prefix=/Applications/MNPP/Library/libxslt    
make    
make install

Gettext
---
wget -c http://ftp.gnu.org/pub/gnu/gettext/gettext-0.18.2.tar.gz    
tar -zxvf gettext-0.18.2.tar.gz    
CFLAGS="-arch i386 -arch x86_64" CXXFLAGS="-arch i386 -arch x86_64" ./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/gettext --with-libiconv-prefix=/Applications/MNPP/Library/$OS_VERSION/libiconv/    
make && make install    

LibMCRYPT
---
wget -c http://downloads.sourceforge.net/project/mcrypt/Libmcrypt/2.5.8/libmcrypt-2.5.8.tar.gz    
tar -zxvf libmcrypt-2.5.8.tar.gz    
./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/mcrypt    
make    
make install

MCRYPT
---
wget -c http://downloads.sourceforge.net/project/mcrypt/MCrypt/2.6.8/mcrypt-2.6.8.tar.gz    
tar -zxvf mcrypt-2.6.8.tar.gz    
./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/mcrypt --with-libmcrypt-prefix=--prefix=/Applications/MNPP/Library/$OS_VERSION/mcrypt    
make    
make install

MHASH
---

wget -c http://downloads.sourceforge.net/project/mhash/mhash/0.9.9.9/mhash-0.9.9.9.tar.bz2    
tar -jxvf mhash-0.9.9.9.tar.bz2   
./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/mhash    
make && make install


Libiconv
---
wget -c http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.14.tar.gz    
CFLAGS="-arch i386 -arch x86_64" CXXFLAGS="-arch i386 -arch x86_64" ./configure --prefix=/Applications/MNPP/Library/libiconv    
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

PHP-MEMCACHE
---
/Applications/MNPP/Library/$OS_VERSION/php52/bin/pecl install memcache
/Applications/MNPP/Library/$OS_VERSION/php53/bin/pecl install memcache
/Applications/MNPP/Library/$OS_VERSION/php54/bin/pecl install memcache

PHP-MEMCACHE FOR PHP52
---
/Applications/MNPP/Library/$OS_VERSION/php52/bin/phpize && ./configure --with-php-config=/Applications/MNPP/Library/$OS_VERSION/php52/bin/php-config --disable-memcache-session  && make && make install

APC
---
/Applications/MNPP/Library/$OS_VERSION/php52/bin/pecl install apc
/Applications/MNPP/Library/$OS_VERSION/php53/bin/pecl install apc
/Applications/MNPP/Library/$OS_VERSION/php54/bin/pecl install apc

MACOSX_DEPLOYMENT_TARGET=10.6 CFLAGS="-arch x86_64 -g -Os -pipe -no-cpp-precomp" CCFLAGS="-arch x86_64 -g -Os -pipe" CXXFLAGS="-arch x86_64 -g -Os -pipe" LDFLAGS="-arch x86_64 -bind_at_load" ./configure --with-php-config=/Applications/MNPP/Library/php{VERSION}/bin/php-config    
make    
cp modules/apc.so /Applications/MNPP/Library/php/lib/php{VERSION}/extensions/no-debug-non-zts-20090626    
add extension=apc.so in php.ini    

APC FOR PHP52
---
/Applications/MNPP/Library/php52/bin/phpize && MACOSX_DEPLOYMENT_TARGET=10.6 CFLAGS="-arch x86_64 -g -Os -pipe -no-cpp-precomp" CCFLAGS="-arch x86_64 -g -Os -pipe" CXXFLAGS="-arch x86_64 -g -Os -pipe" LDFLAGS="-arch x86_64 -bind_at_load" ./configure --with-php-config=/Applications/MNPP/Library/php52/bin/php-config && make && make install

MONGO
---
/Applications/MNPP/Library/$OS_VERSION/php52/bin/pecl install mongo
/Applications/MNPP/Library/$OS_VERSION/php53/bin/pecl install mongo
/Applications/MNPP/Library/$OS_VERSION/php54/bin/pecl install mongo

PHP 2.5.17
---

$ wget -c http://museum.php.net/php5/php-5.2.17.tar.gz
$ tar xvfz php-5.2.17.tar.gz
$ cd php-5.2.17
$ wget -c http://php-fpm.org/downloads/php-5.2.17-fpm-0.5.14.diff.gz
$ gunzip php-5.2.17-fpm-0.5.14.diff.gz
$ patch -p1 < php-5.2.17-fpm-0.5.14.diff

./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/php52 --exec-prefix=/Applications/MNPP/Library/$OS_VERSION/php52 --enable-cli --enable-gd-jis-conv --enable-gd-native-ttf --enable-mbstring --with-bz2 --with-curl=/Applications/MNPP/Library/$OS_VERSION/curl --with-gd=/Applications/MNPP/Library/$OS_VERSION/gd --with-gettext=shared,/Applications/MNPP/Library/$OS_VERSION/gettext --with-freetype-dir=/Applications/MNPP/Library/$OS_VERSION/freetype --with-jpeg-dir=/Applications/MNPP/Library/$OS_VERSION/jpeg --with-libxml-dir=/Applications/MNPP/Library/$OS_VERSION/libxml --with-xsl=/Applications/MNPP/Library/$OS_VERSION/libxslt --with-mcrypt=shared,/Applications/MNPP/Library/$OS_VERSION/mcrypt --with-mhash=/Applications/MNPP/Library/$OS_VERSION/mhash --with-mysql=/Applications/MNPP/Library/$OS_VERSION/mysql --enable-sockets --with-mysqli=/Applications/MNPP/Library/$OS_VERSION/mysql/bin/mysql_config --with-openssl --with-png-dir=/Applications/MNPP/Library/$OS_VERSION/libpng --with-readline --with-ttf --with-xpm-dir=/Applications/MNPP/Library/$OS_VERSION/xpm --with-zlib --with-config-file-path=/Applications/MNPP/conf/php52 --enable-fastcgi --enable-fpm --enable-force-cgi-redirect --with-fpm-conf=/Applications/MNPP/conf/php52/php-fpm --with-fpm-log=/Applications/MNPP/logs/php52/php-fpm.log --with-fpm-pid=/Applications/MNPP/tmp/php52/php-fpm.pid --with-libedit --enable-libxml --enable-dom --with-ncurses=/usr/lib  --enable-pdo --with-pcre-regex --enable-hash --enable-session --enable-json --enable-spl --enable-filter --enable-simplexml --enable-xml --with-iconv=/Applications/MNPP/Library/$OS_VERSION/libiconv --enable-soap
    
make    
make install    

PHP 5.3.22
---
wget -O php53-src.tar.gz http://us2.php.net/get/php-5.3.22.tar.gz/from/this/mirror

tar xvfz php53-src.tar.gz && cd php-5.3.22

brew install pkg-config curl openssl

./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/php53 --exec-prefix=/Applications/MNPP/Library/$OS_VERSION/php53 --enable-cli --enable-gd-jis-conv --enable-gd-native-ttf --enable-mbstring --with-bz2 --with-curl --with-gd --with-gettext=shared,/Applications/MNPP/Library/$OS_VERSION/gettext --with-freetype-dir=/Applications/MNPP/Library/$OS_VERSION/freetype --with-jpeg-dir=/Applications/MNPP/Library/$OS_VERSION/jpeg --with-libxml-dir=/Applications/MNPP/Library/$OS_VERSION/libxml --with-xsl=/Applications/MNPP/Library/$OS_VERSION/libxslt --with-mcrypt=shared,/Applications/MNPP/Library/$OS_VERSION/mcrypt --with-mhash --with-mysql=/Applications/MNPP/Library/$OS_VERSION/mysql --enable-sockets --with-mysqli=/Applications/MNPP/Library/$OS_VERSION/mysql/bin/mysql_config  --with-openssl --with-zlib-dir=/Applications/MNPP/Library/$OS_VERSION/zlib --with-png-dir=/Applications/MNPP/Library/$OS_VERSION/libpng --with-readline --with-xpm-dir=/Applications/MNPP/Library/$OS_VERSION/xpm --with-zlib --with-config-file-path=/Applications/MNPP/conf/php53 --enable-fpm --with-fpm-user=www --with-fpm-group=www --with-libedit --enable-libxml --enable-dom --enable-simplexml --with-iconv=/Applications/MNPP/Library/$OS_VERSION/libiconv --with-pdo-mysql=/Applications/MNPP/Library/$OS_VERSION/mysql/bin/mysql_config  --enable-soap

export EXTRA_CFLAGS=-lresolv

make && make install

PHP 5.4.13
---

Blog Post   
- http://www.devsumo.com/technotes/2013/02/building-php-on-os-x/    
- https://bugs.php.net/bug.php?id=55108   

wget -O php54-src.tar.gz http://us2.php.net/get/php-5.4.13.tar.gz/from/this/mirror

tar xvfz php54-src.tar.gz && cd php-5.4.13

brew install pkg-config curl openssl

./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/php54 --exec-prefix=/Applications/MNPP/Library/$OS_VERSION/php54 --enable-cli --enable-gd-jis-conv --enable-gd-native-ttf --enable-mbstring --with-bz2 --with-curl --with-gd --with-gettext=shared,/Applications/MNPP/Library/$OS_VERSION/gettext --with-freetype-dir=/Applications/MNPP/Library/$OS_VERSION/freetype --with-jpeg-dir=/Applications/MNPP/Library/$OS_VERSION/jpeg --with-libxml-dir=/Applications/MNPP/Library/$OS_VERSION/libxml --with-xsl=/Applications/MNPP/Library/$OS_VERSION/libxslt --with-mcrypt=shared,/Applications/MNPP/Library/$OS_VERSION/mcrypt --with-mhash --with-mysql=/Applications/MNPP/Library/$OS_VERSION/mysql --enable-sockets --with-mysqli=/Applications/MNPP/Library/$OS_VERSION/mysql/bin/mysql_config  --with-openssl-dir=/usr/include/openssl --with-zlib-dir=/Applications/MNPP/Library/$OS_VERSION/zlib --with-png-dir=/Applications/MNPP/Library/$OS_VERSION/libpng --with-readline --with-xpm-dir=/Applications/MNPP/Library/$OS_VERSION/xpm --with-zlib --with-config-file-path=/Applications/MNPP/conf/php54 --enable-fpm --with-fpm-user=www --with-fpm-group=www --with-libedit --enable-libxml --enable-dom --enable-simplexml --with-iconv=/Applications/MNPP/Library/$OS_VERSION/libiconv --with-pdo-mysql=/Applications/MNPP/Library/$OS_VERSION/mysql/bin/mysql_config  --enable-soap

export EXTRA_CFLAGS=-lresolv    
export LC_ALL=en_US.UTF-8   
make && make install

NGINX
---
wget http://downloads.sourceforge.net/project/pcre/pcre/8.32/pcre-8.32.tar.gz && tar xvfz pcre-8.32.tar.gz

curl http://nginx.org/download/nginx-1.2.8.tar.gz | tar -zx && cd nginx-1.2.8   

./configure --prefix=/Applications/MNPP/Library/$OS_VERSION/nginx --sbin-path=/Applications/MNPP/Library/$OS_VERSION/nginx --conf-path=/Applications/MNPP/conf/nginx/nginx.conf --user=www --group=www --with-http_ssl_module --with-http_stub_status_module --pid-path=/Applications/MNPP/run/nginx --with-http_gzip_static_module --with-pcre=/Applications/MNPP/src/pcre-8.32/

make && make install
