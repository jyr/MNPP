--TEST--
APC: APCIterater basic test on file (php 5.4)
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
\$fl = dirname(__FILE__) . '/file.php';
file_put_contents(\$fl, '<?php echo "hello";');
apc_compile_file(\$fl);
\$it = new APCIterator('file');
foreach (\$it as \$i) {
	var_dump(\$i);
}
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
--CLEAN--
unlink(dirname(__FILE__) . '/file.php');
--EXPECTF--
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
array(12) {
  ["type"]=>
  string(4) "file"
  ["filename"]=>
  string(%d) "%sfile.php"
  ["device"]=>
  int(%d)
  ["inode"]=>
  int(%d)
  ["key"]=>
  string(%d) "%d %d"
  ["num_hits"]=>
  int(0)
  ["mtime"]=>
  int(%d)
  ["creation_time"]=>
  int(%d)
  ["deletion_time"]=>
  int(0)
  ["access_time"]=>
  int(%d)
  ["ref_count"]=>
  int(0)
  ["mem_size"]=>
  int(%d)
}
done
