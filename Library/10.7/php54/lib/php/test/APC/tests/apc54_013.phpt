--TEST--
APC: Closures basic test
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
error_reporting(E_ALL);
class Hello
{
	public function say() {
		\$cb = function() {
			return "hello";
		};

		return \$cb();
	}
}

\$h = new Hello;
\$f = function() {return "world";};

var_dump(\$h->say() . ' ' . \$f());
var_dump(\$f);
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

--EXPECTF--
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
string(11) "hello world"
object(Closure)#2 (0) {
}
done
