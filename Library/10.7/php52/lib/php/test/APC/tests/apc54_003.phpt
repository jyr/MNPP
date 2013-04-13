--TEST--
APC: Bug #62190	Couldn't fetch DOMProcessingInstruction with APC and native obj (php 5.4 nts)
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
\$node = new DOMDocument;
\$node->loadHTML('<?foo>');
echo "{\$node->firstChild->nextSibling->nodeType}\n";
FL;

$args = array(
	'apc.enabled=1',
	'apc.enable_cli=1',
	'apc.stat=0',
);

server_start($file, $args);

for ($i = 0; $i < 10; $i++) {
	run_test_simple();
}
echo 'done';


--EXPECT--
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
done
