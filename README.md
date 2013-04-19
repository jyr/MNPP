#MNPP  Mac + Nginx + Percona + PHP
###A high performance web server in a one-click installer.

## Contributors
**This project is currently maintained by the following people:**    

[Jair Gaxiola](https://github.com/jyr) (Core developer)    
[Dmitry Demenchuk](https://github.com/mrded)    
[César Salazar](http://cesarsalazar.mx/)    

**Pull requests authors**

[hmert](https://github.com/hmert)    
[francescolaffi](https://github.com/francescolaffi)    
[gnuget](https://github.com/gnuget)    

##Features

* Start / stop services global
* Open the default page MNPP
* Set preferences - start  / stop global services

##Arch

* x86_64

## Provisions

Needs a update of php, percona or nginx? Only change the software version in bootstrap.sh, example:

	PERCONA_URL='http://www.percona.com/redir/downloads/Percona-Server-5.5/Percona-Server-5.5.30-30.2/source/'
	PERCONA_FILE='Percona-Server-5.5.30-rel30.2'

After run

	sudo sh /Applications/MNPP/provisions/bash/bootstrap.sh

##Set environment

<pre><code>$ sudo sh /Applications/MNPP/init/environment.sh</code></pre>
<pre><code>$ source /Users/youruser/.bash_profile</code></pre>

## Dynamic Extensions

MNPP by default only have mcrypt and gettext enabled, but if  you need more can you install it for each php version, before install autoconf.
	
	$ brew install autoconf

Version: 52 | 53 | 54    

	$ /Applications/MNPP/Library/php[VERSION]/bin/pecl install apc
	
You should add "extension=apc.so" to php.ini

##Runs from console

All    
<pre><code>$ sudo mnpp [Option] [Version]</code></pre>
Only one service    
<pre><code>$ sudo mnpp [Service] [Option]</code></pre>
For php    
<pre><code>$sudo mnpp php [Option] [Version]</code></pre>
Version: 52 | 53 | 54    
Service: nginx | percona | php    
Option: start | stop | restart    


##Percona account

User is root without password the same for phpmyadmin
