--TEST--
APC: Bug #61164 Crash with $_SERVER and ?: operator (php 5.4)
--SKIPIF--
<?php
    require_once(dirname(__FILE__) . '/skipif.inc'); 
    if (PHP_MAJOR_VERSION < 5 || (PHP_MAJOR_VERSION == 5 && PHP_MINOR_VERSION < 4)) {
		die('skip PHP 5.4+ only');
	}
--FILE--
<?php
include "server_test.inc";

$file = <<<FL
\$_SERVER['HTTP_HOST'] ?: "foo";
exit("mommy\n");
FL;

$args = array(
	'apc.enabled=1',
	'apc.cache_by_default=1',
	'apc.enable_cli=1',
);

server_start($file, $args);

for ($i = 0; $i < 10; $i++) {
	run_test_simple();
}
echo 'done';
--EXPECT--
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
mommy
done
