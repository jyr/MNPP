--TEST--
APC: bug #62302 apc.include_once_override=1 made everything crash
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
	echo 1 == 1 ? sprintf("%s\n","This is me") : sprintf("%s\n","This is not me");
FL;

$args = array(
	'apc.enabled=1',
	'apc.enable_cli=1',
	'apc.include_once_override=1',
);

server_start($file, $args);

for ($i = 0; $i < 10; $i++) {
	run_test_simple();
}
echo 'done';


--EXPECTF--
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
This is me
done
