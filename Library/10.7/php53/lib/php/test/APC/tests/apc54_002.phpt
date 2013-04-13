--TEST--
APC: interned strings same method names (php 5.4 nts)
--SKIPIF--
<?php
    require_once(dirname(__FILE__) . '/skipif.inc'); 
    if (PHP_MAJOR_VERSION < 5 || (PHP_MAJOR_VERSION == 5 && PHP_MINOR_VERSION < 4)) {
		die('skip PHP 5.4+ only');
	}
	if (PHP_ZTS) {
		die('skip NTS only');
	}
--FILE--
<?php
include "server_test.inc";

$file = <<<FL
function hello()
{
	echo "hello function\n";
}

class one {
	protected \$hello;
	function hello() {
		echo "hello class one\n";
	}
}

class two {
	public \$hello;
	function hello() {
		echo "hello class two\n";
	}
}

\$one = new one;
\$two = new two;
\$one->hello();
\$two->hello();
hello();
FL;

$args = array(
	'apc.enabled=1',
	'apc.enable_cli=1',
	'apc.stat=0',
);

server_start($file, $args);

list($host, $port) = explode(':', PHP_CLI_SERVER_ADDRESS);
$port = intval($port)?:80;

for ($i = 0; $i < 10; $i++) {
	run_test_simple();
}
echo 'done';

--EXPECT--
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
hello class one
hello class two
hello function
done
