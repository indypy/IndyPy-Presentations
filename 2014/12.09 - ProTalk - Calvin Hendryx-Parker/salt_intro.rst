:title: IndyPy Intro to SaltStack

----

IndyPy Intro to SaltStack
=========================

December 9th, 2014

----

What is **Salt**?
=================

* Remote Execution
* Configuration Management
* Orchestration
* Plus Tons To Discover

.. note::

    Written in Python and uses ZeroMQ
    Secure bi-directional communication
    Masters, Minions and even Masterless and Multi-Masters
    We won't even get into Reactors and Events
    Super flexible tool

----

Why do I need such a thing?
===========================

* Consistency
* Scalability
* Speed

.. note::

    Roll out to thousands of servers in seconds
    Ensure configs are what you expect
    Security issues make rolling out configs and new packages a more frequent task
    No need to touch the servers, do everything via Salt

----

Salty Jargon
============

* Master
* Minion
* Modules
* States
* Grains
* Pillars
* Targeting
* Formulas
* Jobs

.. note::

    Targeting can be via glob, regex, grains, pillars, IP, Compound and Nodegroup
    Formulas are sets of states served over the salt fileserver
    There are other terms for later like Salt Mine for gathering data from minons at the master to make it available back to all minions
    and Syndics for relaying messages between tiered masters

----

Getting Started
===============

* https://github.com/saltstack/salt-bootstrap
* Platform Repos
* Install Master
* Install Minion

.. note::

    Salt package is available for most platforms via your pkg mgmt tool
    They have a collection of one/two line bootstrap scripts that will work about anywhere
    the Bootstrap will allow you to install any tag/branch of the project
    Minion only needs the address of the Master
    By default it will look for a host called *Salt*
    A minion will generate an ID autmatically based on hostname, DNS and falls back to localhost
    You can override the ID

----

Minion Authentication
=====================

* Public-Key Encryption
* ``salt-key`` Manages Keys
* Pre-Seeding
* Open Masters

.. note::

    You can check the fingerprints on master and minion to ensure they match before accepting keys

----

Let's get to work
=================

Remote Execution
----------------

* Salt Execution Modules
* Modules Contain Functions
* You Target Minions

.. note::

    test.ping
    test.version
    targeting uses globs, regexes and grains, compound, nodegroups
    status.version
    status.w
    status.loadavg
    grains.items
    grains.get os_family
    iptables.get_rules
    

----

Keep it Together
================

Configuration Management
------------------------

* Salt States
* YAML
* Jinja Templates

.. note::

    Specify the state your machines should be in
    top.sls defines what boxes get what states
    Use grains to conditionally configure
    Use Requisites to specify execution order
    install nginx
    add a user

----

Thanks!
=======

-----
