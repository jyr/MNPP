--TEST--
APC: Bug #62456	Incorrect description of notice variation 1 (php 5.4 nts)
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
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
<br />
<b>Notice</b>:  Undefined property: stdClass::$qwerty in <b>/home/weltling/dws/src/apc_trunk/tests/index.php</b> on line <b>3</b><br />
done
