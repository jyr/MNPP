--TEST--
APC: Bug #59907	Issue with custom stream wrapper, include and APC
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
class StreamWrapper {
    const PROTOCOL = 'mfx';
    
    private static \$data = array();
    private \$path = null;
    private \$position = 0;
    
    public function stream_open(\$path, \$mode , \$options , &\$opened_path) {
        
        \$this->path = \$path;
        
        return true;
    }
            	
    public function stream_read(\$count) {
        
        \$ret = substr(self::\$data[\$this->path], \$this->position, \$count);
        \$this->position += strlen(\$ret);
        
        return \$ret;
    }
    
    public function stream_write(\$data) {
        
        self::\$data[\$this->path] = \$data;
        
        return strlen(\$data);
    }
    
    public function stream_tell() {
        
        return \$this->position;
    }
    
    public function stream_eof() {
        
        return \$this->position >= strlen(self::\$data[\$this->path]);
    }
    
    public function url_stat(\$path, \$flags) {
        
        return \$this->stream_stat();
    }
    
    public function stream_stat() {
        
        \$stat = array(
            'dev' => 1,
            'ino' => 1,
            'mode' => 1,
            'nlink' => 1,
            'uid' => 1,
            'gid' => 1,
            'rdev' => 1,
            'size' => 1,
            'atime' => 1,
            'mtime' => 1,
            'ctime' => 1,
            'blksize' => 1,
            'blocks' => 1
        );
        
        return array_merge(array_values(\$stat), \$stat);
    }
}

stream_wrapper_register(StreamWrapper::PROTOCOL, 'StreamWrapper');

\$class1 = '<?php class test1 {function __construct(){echo "test1\n";}}';
\$class2 = '<?php class test2 {function __construct(){echo "test2\n";}}';

file_put_contents('mfx://test1', \$class1);
file_put_contents('mfx://test2', \$class2);

include 'mfx://test1';
include 'mfx://test2';

new test1;
new test2;

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
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
test1
test2
done
