--TEST--
APC: Bug #62419	RuntimeException throws fatal error if passing a previous exception to the ctor (php 5.4)
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
throw new RuntimeException("Exception message", 0, new Exception());
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
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Exception' in %sindex.php:2
Stack trace:
#0 {main}

Next exception 'RuntimeException' with message 'Exception message' in %sindex.php:2
Stack trace:
#0 {main}
  thrown in <b>%sindex.php</b> on line <b>2</b><br />
done
