:title: Manage Your App with Circus
:author: David Blewett
:description: How to use Circus to manage process, sockets and network connections
:keywords: python, circus, zmq, ssh
:css: circus.css

----

Manage Your App with
====================

.. image:: images/circus-medium.png

Does your application have multiple moving parts? Have you wanted it to start at boot,
but ran away screaming from Upstart or heaven forbid, daemontools? Are you annoyed by
having to use different tools to manage your web processes and other pieces of your app?
Circus might be for you!

----

Key Points
==========

* What Circus is
* Comparison to other systems
* How to deploy it
* Examples

----

What is it?
===========

* Python daemon
* Monitor / control processes (and sockets!)
* CLI, web UI, Python API
* Developed by Tarek Ziadé
* Used extensively by Mozilla

----

What is it?
===========

.. image:: images/circus-architecture.png

----

Glossary
========

*arbiter*
  The arbiter is responsible for managing all the watchers within circus, ensuring all processes run correctly.
*controller*
  A controller contains the set of actions that can be performed on the arbiter.

----

Glossary
========

*watcher*
  A watcher is the program you tell Circus to run. A single Circus instance can run one or more watchers.
*process/worker*
  A process is an independent OS process instance of your program. A single watcher can run one or more processes.

----

Glossary
========

*remote controller*
  The remote controller allows you to communicate with the controller via ZMQ to control Circus.
*flapping*
  The flapping detection subscribes to events and detects when some processes are constantly restarting.
*pub/sub*
  Circus has a channel that receives events from the watchers and dispatches them to all subscribers.

----

Similar Tools
=============

* Upstart_
* Supervisord_
* daemontools_

.. _Upstart: http://upstart.ubuntu.com/
.. _Supervisord: http://supervisord.org/
.. _daemontools: http://cr.yp.to/daemontools.html

----

Similar Tools
=============

.. role:: strike
    :class: strike

* Upstart_
* Supervisord_
* :strike:`daemontools`

.. _Upstart: http://upstart.ubuntu.com/
.. _Supervisord: http://supervisord.org/

----

Comparison: Classical
=====================

.. image:: images/classical-stack.png

----

Comparison: Circus
==================

.. image:: images/circus-stack.png

----

Supervisord
===========

Pros:

* Mature, well-established codebase
* Rich CLI
* Flexible configuration

Cons:

* Stagnating development
* Hard to track down bugs

----

Circus
======

Pros:

* Accelerating development
* Extensive deployments
* More flexible integration

Cons:

* CLI not as flexible
* Configuration lacks some features (grouping)

----

Configuration
=============

* INI (``ConfigParser``) style
* Root ``[circus]`` section configures global functionality
* Any number of ``watcher`` sections
* Any number of ``env`` sections for a specific ``watcher``
* Any number of ``socket`` sections
* Any number of ``plugin`` sections

----

Simple Example
==============

.. code:: ini

    [circus]
    stats_endpoint = tcp://127.0.0.1:5557
    httpd = 1
    httpd_host = 127.0.0.1
    httpd_port = 8000
    
    [watcher:web]
    cmd = chaussette --fd $(circus.sockets.web) --backend meinheld server.app
    use_sockets = True
    numprocesses = 3
    
    [socket:web]
    host = 0.0.0.0
    port = 8080

    [watcher:redis]
    cmd = /usr/local/bin/redis-server /usr/local/etc/redis.conf
    singleton = 1

----

How do I use it?
================

* Point Circus at directory of config files
  
  * Via ``include_dir``

* Buildout generates templates for services on host:

    .. code:: sh
    
        /buildout-dir/circus.ini
        /buildout-dir/circus.d
        /buildout-dir/circus.d/bar.ini
        /buildout-dir/circus.d/baz.ini
        /buildout-dir/circus.d/foo.ini

----

How do I use it?
================

* Circus controls:
 
 * ZMQ processing pipeline
 * SSH Tunnels (using ``keychain``)
 * Web workers
 * ElasticSearch
 * Memcached

----

Start at Boot (stock)
=====================

.. code:: sh

    start on filesystem and net-device-up IFACE=lo
    
    stop on shutdown
    
    respawn
    exec /usr/local/bin/circusd \
        --log-output /var/log/circus.log \
        --pidfile /var/run/circusd.pid \
        /etc/circus.ini

----

Start at Boot (SSH)
===================

.. code:: sh

    start on filesystem and net-device-up IFACE=lo
    
    stop on shutdown
    
    respawn
    exec su -s /bin/sh -c 'exec "$0" "$@"' -l csoc -- \
        /path/to/circusd \
        --log-output /var/log/circus.log \
        --pidfile /var/circusd.pid \
        /path/to/buildout/etc/circus.ini

----

SSH Example
===========


.. code:: ini

    [watcher:ssh_tunnel]
    cmd = /usr/bin/ssh
    args = -C -N -o ServerAliveInterval=30 -o ExitOnForwardFailure=yes
           -i /path/to/privkey -L 6001:127.0.0.1:3306 user@my.ip.address
    singleton = True
    priority = 1
    copy_env = True
    
----

References
==========

* https://circus.readthedocs.org_
* http://en.wikipedia.org/wiki/Fork-exec_
* https://chaussette.readthedocs.org
* http://www.funtoo.org/Keychain

.. _circus.readthedocs.org: https://circus.readthedocs.org
.. _fork-exec: http://en.wikipedia.org/wiki/Fork-exec
.. _chaussette.readthedocs.org: https://chaussette.readthedocs.org
.. _Keychain: http://www.funtoo.org/Keychain
