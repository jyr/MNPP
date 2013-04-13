--TEST--
APC: Bug #61219	method not found on 2nd request (php 5.4)
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
\$there = 'world';

class hello
{
    function __construct(\$p)
    {   
        \$this->testme(\$p);
    }   

    function testme(\$p)
    {   
        echo "testme \$p\n";
    }   
}

\$h = new hello(\$there);
FL;

$args = array(
	'apc.enabled=1',
	'apc.cache_by_default=1',
	'apc.enable_cli=1',
	'apc.slam_defense=0',
	'apc.write_lock=1',
);

server_start($file, $args);

for ($i = 0; $i < 10; $i++) {
	run_test_simple();
}
echo 'done';
--EXPECT--
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
testme world
done
