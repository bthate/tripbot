TRIPBOT
#######

| Welcome to TRIPBOT , 24/7 channel daemon - 

TRIPBOT is a pure python3 IRC chat bot that can run as a background daemon
for 24/7 a day presence in a IRC channel. It installs itself as a service so
you can get it restarted on reboot. You can use it to display RSS feeds, act as a
UDP to IRC gateway, program your own commands for it, have it log objects on
disk and search them and scan emails for correspondence analysis. TRIPBOT uses
a JSON in file database with a versioned readonly storage. It reconstructs
objects based on type information in the path and uses a "dump OOP and use
OP" programming library where the methods are factored out into functions
that use the object as the first argument. 

TRIPBOT is placed in the Public Domain and has no COPYRIGHT or LICENSE.

INSTALL
=======

you can download with pip3 and install globally:

::

 > sudo pip3 install tripbot --upgrade --force-reinstall

in case of emergency, remove all tripbot packages from system:

 : sudo rm -fR /usr/local/lib/python3.8/dist-packages/tripbot*

and try installing from onto a fresh system. You can also download the tarball
and run/install from that, see https://pypi.org/project/tripbot/#files

SERVICE
=======

To run TRIPBOT as a service, the setup.py creates a tripbot user and group
installs the /etc/systemd/system/tripbot.service if it is not already there.
It doesn't get enabled on default, to do so run the following:

::

 $ sudo systemctl enable tripbot
 $ sudo systemctl daemon-reload

This enables the rebooting of TRIPBOT. To have it connected to the right
server and channel run the cfg command:

::

 $ sudo tripbot cfg server=irc.freenode.net channel=\#dunkbots
nick=tripbot

Restart the service:

::

 $ sudo service tripbot stop
 $ sudo service tripbot start

If you don't want the tripbot to startup at boot, disable the service:

::

 $ sudo systemctl disable tripbot

RSS
===

TRIPBOT provides with the use of feedparser the possibility to server rss
feeds in your channel. TRIPBOT itself doesn't depend, you need to install
python3-feedparser first:

::

 $ sudo apt install python3-feedparser
 $

to add an url use the rss command with an url:

::

 $ sudo tripbot rss https://github.com/bthate/tripbot/commits/master.atom
 ok 1

run the rss command to see what urls are registered:

::

 $ sudo tripbot fnd rss
 0 https://github.com/bthate/tripbot/commits/master.atom

the ftc (fetch) command can be used to poll the added feeds:

::

 $ sudo tripbot ftc
 fetched 20

UDP
===

TRIPBOT also has the possibility to serve as a UDP to IRC relay where you
can send UDP packages to the bot and have txt displayed on the channel.

use the `tripbot udp` command to send text via the bot to the channel on the irc 
server:

::

 $ tail -f /var/log/syslog | tripbot udp

to send the tail output to the IRC channel

you can use python3 code to send a UDP packet to the bot, it's unencrypted
txt send to the bot and display on the joined channels.

to send a udp packet to tripbot in python3:

::

 import socket

 def toudp(host=localhost, port=5500, txt=""):
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     sock.sendto(bytes(txt.strip(), "utf-8"), host, port)

OBJECT PROGRAMMING
==================

TRIPBOT uses "object programming that provides a "move all methods to functions"
programming style like this:

::

 obj.method(*args) -> method(obj, *args) 

 e.g.

 not:

 >>> from obj import Object
 >>> o = Object()
 >>> o.set("key", "value")
 >>> o.key
 'value'

 but:

 >>> from obj import Object, set
 >>> o = Object()
 >>> set(o, "key", "value")
 >>> o.key
 'value'

it's a way of programming with objects, replacing OOP. Not object-oriented 
programming, but object programming. If you are used to functional 
programming you'll like it (or not) ;]

MODULES
=======

TRIPBOT use the following modules for object loading/saving (config files) and
event handler/console code/cli parsing:

::

    bus          - announce
    cfg          - config
    cms          - commands
    csl          - console
    dbs          - databases
    dft          - default
    ent          - entry
    fnd          - find
    evt          - event
    hdl          - handler
    irc          - internet relay chat
    itr          - introspection
    krn          - kernel
    mbx          - mailbox
    obj          - objects
    obl          - list of objects
    ofn          - object functions
    prs          - parser
    rss          - rich site syndicate
    tms          - times
    trm          - terminal
    tsk          - tasks
    udp          - udp to irc relay
    utl          - utilities

have fun coding !!

CONTACT
=======

"contributed back to society" 

you can contact me on IRC/freenode/#dunkbots or email me at bthate@dds.nl

| Bart Thate (bthate@dds.nl, thatebart@gmail.com)
| botfather on #dunkbots irc.freenode.net 

