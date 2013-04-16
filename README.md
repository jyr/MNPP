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

##Set environment

<pre><code>$ sudo sh /Applications/MNPP/init/environment.sh</code></pre>
<pre><code>$ source /Users/youruser/.bash_profile</code></pre>

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
