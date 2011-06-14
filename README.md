#MNPP  Mac + Nginx + Percona + PHP or Python
###A high performance web server in a one-click installer.

## Contributors
**This project is currently maintained by the following people:**    

[Jair Gaxiola](https://github.com/jyr) (Core developer)    
[César Salazar](http://cesarsalazar.mx/)    
[Astrata Software](http://astrata.mx)

##Features

* Start / stop services global
* Start / stop services individually
* Open the default page MNPP
* Set preferences - start  / stop global services

##Arch

* x86_64

##Runs from console

Start    
<pre><code>$ sudo mnpp --php[Version] --start</code></pre>
Start only one service    
<pre><code>$ sudo mnpp --start [service]</code></pre>
For php    
<pre><code>$ sudo mnpp --start php[Version]</code></pre>
version: 52 | 53    
service: nginx | percona | uwsgi

Stop    
<pre><code>$ sudo mnpp --php[Version] --stop</code></pre>
Stop only one service    
<pre><code>$ sudo mnpp --stop [service]</code></pre>
For php    
<pre><code>$ sudo mnpp --stop php[Version]</code></pre>

version: 52 | 53    
service: nginx | percona | uwsgi

##Percona account

User is root without password the same for phpmyadmin
