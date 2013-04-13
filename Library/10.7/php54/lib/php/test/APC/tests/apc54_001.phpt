--TEST--
APC: bug #62398 (php 5.4)
--SKIPIF--
<?php
    require_once(dirname(__FILE__) . '/skipif.inc'); 
    if (PHP_MAJOR_VERSION < 5 || (PHP_MAJOR_VERSION == 5 && PHP_MINOR_VERSION < 4)) {
		die('skip for PHP >= 5.4');
	}
--FILE--
<?php
include "server_test.inc";

file_put_contents(dirname(__FILE__) . '/base.php', "<?php\nclass FOO{}\necho 'hello\n';");

$args = array(
	'apc.enabled=1',
	'apc.enable_cli=1',
	'apc.stat=0',
	'apc.shm_size=50M',
	'apc.max_file_size=1M',
	'apc.ttl=0',
	'apc.gc_ttl=3600',
	'apc.file_update_protection=0',
	'apc.cache_by_default=1',
	'apc.include_once_override=0',
	'apc.localcache=0',
	'apc.localcache.size=512',
	'apc.num_files_hint=1000',
	'apc.report_autofilter=0',
	'apc.rfc1867=0',
	'apc.slam_defense=0',
	'apc.stat=0',
	'apc.stat_ctime=0',
	'apc.write_lock=1',
);
server_start('include "base.php";', $args);

list($host, $port) = explode(':', PHP_CLI_SERVER_ADDRESS);
$port = intval($port)?:80;

$send = "GET / HTTP/1.1\nHost: {$host}\r\n\r\n";
for ($i = 0; $i < 5; $i++) {
	run_test($host, $port, $send);
}
echo 'done';

--CLEAN--
<?php
//	unlink(dirname(__FILE__) . '/base.php');
--EXPECTF--
hello
hello
hello
hello
hello
done
