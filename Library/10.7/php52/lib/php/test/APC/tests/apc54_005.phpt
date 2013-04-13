--TEST--
APC: Bug #62456	Incorrect description of notice variation 2 (php 5.4 nts)
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
set_error_handler(function(\$errno, \$errstr, \$errfile, \$errline){
	throw new ErrorException(\$errstr, 0, \$errno, \$errfile, \$errline);
});
\$test = new StdClass();
echo \$test->qwerty;
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
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'ErrorException' with message 'Undefined property: stdClass::$qwerty' in %sindex.php:6
Stack trace:
#0 %sindex.php(6): {closure}(8, 'Undefined prope...', '%s', 6, Array)
#1 {main}
  thrown in <b>%sindex.php</b> on line <b>6</b><br />
done
