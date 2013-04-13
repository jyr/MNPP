--TEST--
APC: Bug #61515 Cached script shows different result from uncached (php 5.4)
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
abstract class Dog {
    public abstract function bark();
}
abstract class SmallDog extends Dog {
}
class Charlie extends SmallDog {
    function bark() {
        echo "woof!\n";
    }
}
\$charlie = new Charlie();
\$charlie->bark();
FL;

$args = array(
	'apc.enabled=1',
	'apc.enable_cli=1',
);

server_start($file, $args);

for ($i = 0; $i < 10; $i++) {
	run_test_simple();
}
echo 'done';

--EXPECT--
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
woof!
done
