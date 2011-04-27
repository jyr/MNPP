/*                                                                -*- C -*-
   +----------------------------------------------------------------------+
   | PHP Version 5                                                        |
   +----------------------------------------------------------------------+
   | Copyright (c) 1997-2007 The PHP Group                                |
   +----------------------------------------------------------------------+
   | This source file is subject to version 3.01 of the PHP license,      |
   | that is bundled with this package in the file LICENSE, and is        |
   | available through the world-wide-web at the following url:           |
   | http://www.php.net/license/3_01.txt                                  |
   | If you did not receive a copy of the PHP license and are unable to   |
   | obtain it through the world-wide-web, please send a note to          |
   | license@php.net so we can mail you a copy immediately.               |
   +----------------------------------------------------------------------+
   | Author: Stig Sæther Bakken <ssb@php.net>                             |
   +----------------------------------------------------------------------+
*/

/* $Id: build-defs.h.in 292156 2009-12-15 11:17:47Z jani $ */

#define CONFIGURE_COMMAND " './configure'  '--prefix=/Applications/MNPP/Library/php52' '--exec-prefix=/Applications/MNPP/Library/php52' '--enable-cli' '--enable-gd-jis-conv' '--enable-gd-native-ttf' '--enable-mbstring' '--with-bz2' '--with-curl=/Applications/MNPP/Library/curl' '--with-gd=/Applications/MNPP/Library/gd' '--with-gettext=shared,/Applications/MNPP/Library/gettext' '--with-freetype-dir=/Applications/MNPP/Library/freetype' '--with-jpeg-dir=/Applications/MNPP/Library/jpeg' '--with-libxml-dir=/Applications/MNPP/Library/libxml' '--with-xsl=/Applications/MNPP/Library/libxslt' '--with-mcrypt=shared,/Applications/MNPP/Library/mcrypt' '--with-mhash' '--with-mysql=/Applications/MNPP/Library/mysql' '--enable-sockets' '--with-mysqli=/Applications/MNPP/Library/mysql/bin/mysql_config' '--with-openssl' '--with-png-dir=/Applications/MNPP/Library/libpng' '--with-readline' '--with-ttf' '--with-xpm-dir=/Applications/MNPP/Library/xpm' '--with-zlib' '--with-config-file-path=/Applications/MNPP/conf/php52' '--enable-fastcgi' '--enable-fpm' '--enable-force-cgi-redirect' '--with-fpm-conf=/Applications/MNPP/conf/php52/php-fpm' '--with-fpm-log=/Applications/MNPP/logs/php52/php-fpm.log' '--with-fpm-pid=/Applications/MNPP/tmp/php52/php-fpm.pid' '--with-libedit' '--enable-libxml' '--enable-dom' '--with-ncurses=/usr/lib' '--enable-pdo' '--with-pcre-regex' '--disable-all'"
#define PHP_ADA_INCLUDE		""
#define PHP_ADA_LFLAGS		""
#define PHP_ADA_LIBS		""
#define PHP_APACHE_INCLUDE	""
#define PHP_APACHE_TARGET	""
#define PHP_FHTTPD_INCLUDE      ""
#define PHP_FHTTPD_LIB          ""
#define PHP_FHTTPD_TARGET       ""
#define PHP_CFLAGS		"$(CFLAGS_CLEAN) -prefer-non-pic -static"
#define PHP_DBASE_LIB		""
#define PHP_BUILD_DEBUG		""
#define PHP_GDBM_INCLUDE	""
#define PHP_IBASE_INCLUDE	""
#define PHP_IBASE_LFLAGS	""
#define PHP_IBASE_LIBS		""
#define PHP_IFX_INCLUDE		""
#define PHP_IFX_LFLAGS		""
#define PHP_IFX_LIBS		""
#define PHP_INSTALL_IT		"@echo "Installing PHP CGI binary: $(INSTALL_ROOT)$(bindir)/"; $(INSTALL) -m 0755 $(SAPI_CGI_PATH) $(INSTALL_ROOT)$(bindir)/$(program_prefix)php-cgi$(program_suffix)$(EXEEXT)"
#define PHP_IODBC_INCLUDE	""
#define PHP_IODBC_LFLAGS	""
#define PHP_IODBC_LIBS		""
#define PHP_MSQL_INCLUDE	""
#define PHP_MSQL_LFLAGS		""
#define PHP_MSQL_LIBS		""
#define PHP_MYSQL_INCLUDE	"-I/Applications/MNPP/Library/mysql/include/mysql"
#define PHP_MYSQL_LIBS		"-L/Applications/MNPP/Library/mysql/lib/mysql -lmysqlclient "
#define PHP_MYSQL_TYPE		"external"
#define PHP_ODBC_INCLUDE	""
#define PHP_ODBC_LFLAGS		""
#define PHP_ODBC_LIBS		""
#define PHP_ODBC_TYPE		""
#define PHP_OCI8_SHARED_LIBADD 	""
#define PHP_OCI8_DIR			""
#define PHP_OCI8_VERSION		""
#define PHP_ORACLE_SHARED_LIBADD 	"@ORACLE_SHARED_LIBADD@"
#define PHP_ORACLE_DIR				"@ORACLE_DIR@"
#define PHP_ORACLE_VERSION			"@ORACLE_VERSION@"
#define PHP_PGSQL_INCLUDE	""
#define PHP_PGSQL_LFLAGS	""
#define PHP_PGSQL_LIBS		""
#define PHP_PROG_SENDMAIL	"/usr/sbin/sendmail"
#define PHP_SOLID_INCLUDE	""
#define PHP_SOLID_LIBS		""
#define PHP_EMPRESS_INCLUDE	""
#define PHP_EMPRESS_LIBS	""
#define PHP_SYBASE_INCLUDE	""
#define PHP_SYBASE_LFLAGS	""
#define PHP_SYBASE_LIBS		""
#define PHP_DBM_TYPE		""
#define PHP_DBM_LIB		""
#define PHP_LDAP_LFLAGS		""
#define PHP_LDAP_INCLUDE	""
#define PHP_LDAP_LIBS		""
#define PHP_BIRDSTEP_INCLUDE     ""
#define PHP_BIRDSTEP_LIBS        ""
#define PEAR_INSTALLDIR         ""
#define PHP_INCLUDE_PATH	".:"
#define PHP_EXTENSION_DIR       "/Applications/MNPP/Library/php52/lib/php/extensions/no-debug-non-zts-20060613"
#define PHP_PREFIX              "/Applications/MNPP/Library/php52"
#define PHP_BINDIR              "/Applications/MNPP/Library/php52/bin"
#define PHP_SBINDIR             "/Applications/MNPP/Library/php52/sbin"
#define PHP_LIBDIR              "/Applications/MNPP/Library/php52/lib/php"
#define PHP_DATADIR             "/Applications/MNPP/Library/php52/share/php"
#define PHP_SYSCONFDIR          "/Applications/MNPP/Library/php52/etc"
#define PHP_LOCALSTATEDIR       "/Applications/MNPP/Library/php52/var"
#define PHP_CONFIG_FILE_PATH    "/Applications/MNPP/conf/php52"
#define PHP_CONFIG_FILE_SCAN_DIR    ""
#define PHP_SHLIB_SUFFIX        "so"
