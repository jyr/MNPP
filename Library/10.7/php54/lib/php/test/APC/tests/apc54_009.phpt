--TEST--
APC: Bug #61824 apc produces strange notice (php 5.4)
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
ini_set('display_errors', 1);
\$d = new DOMDocument;
\$d = new DOMXPath(\$d);
var_export(\$d->document);
echo "\n";
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
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
DOMDocument::__set_state(array(
))
done
