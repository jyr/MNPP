--TEST--
APC: Bug #61912 Memory corruption in ext/dom (php 5.4)
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
\$doc = new DOMDocument();
\$doc->loadXML('<?xml version="1.0" encoding="UTF-8"?><root/>');

\$xpath = new DOMXPath(\$doc);
\$namespaces = \$xpath->query('namespace::*');

var_dump(\$namespaces->item(0));
print \$namespaces->item(0)->localName;
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
object(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmlobject(DOMNameSpaceNode)#3 (8) {
  ["nodeName"]=>
  string(9) "xmlns:xml"
  ["nodeValue"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["nodeType"]=>
  int(18)
  ["prefix"]=>
  string(3) "xml"
  ["localName"]=>
  string(3) "xml"
  ["namespaceURI"]=>
  string(36) "http://www.w3.org/XML/1998/namespace"
  ["ownerDocument"]=>
  string(22) "(object value omitted)"
  ["parentNode"]=>
  string(22) "(object value omitted)"
}
xmldone
