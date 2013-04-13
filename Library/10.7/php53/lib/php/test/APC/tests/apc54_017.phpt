--TEST--
APC: Test use trait properties in a class and its parent (php 5.4)
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
trait ParentHello
{
	protected \$three = 'parent trait';
}

trait Hello
{
	protected \$one = 'trait';
}

class ParentWorld
{
	use ParentHello;
	protected \$two = 'parent';
}

class World extends ParentWorld
{
	use Hello;
	protected \$me = 'self';
	public function loud()
	{
		return \$this->me . ' | ' . \$this->one . ' | ' . \$this->two . ' | ' . \$this->three;
	}
}

\$w = new World;
var_dump(\$w->loud());
FL;

$args = array(
'apc.cache_by_default=On',
'apc.canonicalize=On',
'apc.coredump_unmap=Off',
'apc.enable_cli=On',
'apc.enabled=On',
'apc.file_md5=Off',
'apc.file_update_protection=2',
'apc.filters=no',
'apc.gc_ttl=3600',
'apc.include_once_override=Off',
'apc.lazy_classes=Off',
'apc.lazy_functions=Off',
'apc.max_file_size=1M',
'apc.mmap_file_mask=no',
'apc.num_files_hint=1000',
'apc.preload_path=no',
'apc.report_autofilter=Off',
'apc.rfc1867=Off',
'apc.rfc1867_freq=0',
'apc.rfc1867_name=APC_UPLOAD_PROGRESS',
'apc.rfc1867_prefix=upload_',
'apc.rfc1867_ttl=3600',
'apc.serializer=default',
'apc.shm_segments=1',
'apc.shm_size=128M',
'apc.shm_strings_buffer=4M',
'apc.slam_defense=On',
'apc.stat=On',
'apc.stat_ctime=Off',
'apc.ttl=0',
'apc.use_request_time=On',
'apc.user_entries_hint=4096',
'apc.user_ttl=0',
'apc.write_lock=On',
);

server_start($file, $args);

for ($i = 0; $i < 10; $i++) {
	run_test_simple();
}
echo 'done';

--EXPECT--
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
string(36) "self | trait | parent | parent trait"
done
