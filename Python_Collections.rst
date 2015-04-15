.. -*- coding: utf-8 -*-

:title: Python Collections
:event: IndyPy
:author: Calvin Hendryx-Parker
:pygments: tango

.. |space| unicode:: 0xA0 .. non-breaking space
.. |br| raw:: html

    <br />

----

Python Collections
==================

(or make your life easier and your code faster)
+++++++++++++++++++++++++++++++++++++++++++++++

Calvin Hendryx-Parker, IndyPy April 2015
----------------------------------------

.. note::

    Seems little used, but it incredibly handy. Python Collections are Container data types.

----

What's in the package?
======================

* namedtuple
* deque
* ChainMap
* Counter
* OrderedDict
* defaultdict
* UserDict
* UserList
* UserString

.. note::

    Collections was added in Python 2.4

----

namedtuple
==========

.. code:: python

    import collections

    Person = collections.namedtuple('Person', 'name age gender')
    
    print 'Type of Person:', type(Person)
    
    bob = Person(name='Bob', age=30, gender='male')
    print '\nRepresentation:', bob
    
    jane = Person(name='Jane', age=29, gender='female')
    print '\nField by name:', jane.name
    
    print '\nFields by index:'
    for p in [ bob, jane ]:
        print '%s is a %d year old %s' % p


.. note::

    Standard tuples use numerical indexes to access its members.

    If your data has an order that matters, it would be nice if you could access them by a meaningful name.

    Just as memory efficient as regular tuples because they do not have per-instance dictionaries.

    Creates a new class, which is the first argument to the constructor.

    You will get ValueErrors if you try to use an invalid name such as a reserved keyword.

    Can be worked around with "rename=True", but you get generated names of an index prefixed by an _ as of 3.1

----

namedtuple with CSV and sqlite
==============================

.. code:: python

    from collections import namedtyple
    import csv
    import sqlite3


    EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
    
    for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
        print(emp.name, emp.title)
    
    conn = sqlite3.connect('/companydata')
    cursor = conn.cursor()
    cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
    for emp in map(EmployeeRecord._make, cursor.fetchall()):
        print(emp.name, emp.title)

.. note::

    _make -- Class method that makes a new instance from an existing sequence or iterable.
    
    Also possible to get back the object as an OrderedDict, reg dict prior to 3.1

----

deque
=====

.. code:: python

    import collections

    # Add to the right
    d = collections.deque()
    d.extend('abcdefg')
    print 'extend    :', d
    d.append('h')
    print 'append    :', d
    
    # Add to the left
    d = collections.deque()
    d.extendleft('abcdefg')
    print 'extendleft:', d
    d.appendleft('h')
    print 'appendleft:', d

.. note::

    Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction

    Consume from both sides from multiple threads

    For fast random access, use lists instead.

----

deque
=====

.. code:: python

    def tail(filename, n=10):
        'Return the last n lines of a file'
        with open(filename) as f:
            return deque(f, n)

.. note::

    example of simulating the tail command in python

----

ChainMap
========

.. code:: python

    from collections import ChainMap
    import builtins
    pylookup = ChainMap(locals(), globals(), vars(builtins))

.. code:: python

    from collections import ChainMap
    import os, argparse

    defaults = {'color': 'red', 'user': 'guest'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k:v for k, v in vars(namespace).items() if v}

    combined = ChainMap(command_line_args, os.environ, defaults)


.. note::

    New in 3.3

----

Counter
=======

.. code:: python

    from collections import Counter
    import re

    words = re.findall(r'\w+', open('hamlet.txt').read().lower())
    print(Counter(words).most_common(10))

.. code:: python

    >>> [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

.. note::

    A Counter is a container that keeps track of how many times equivalent values are added.

----

Handy Counter Tricks
====================

.. code:: python

    sum(c.values())                 # total of all counts
    c.clear()                       # reset all counts
    list(c)                         # list unique elements
    set(c)                          # convert to a set
    dict(c)                         # convert to a regular dictionary
    c.items()                       # convert to a list of (elem, cnt) pairs
    Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
    c.most_common()[:-n-1:-1]       # n least common elements
    +c                              # remove zero and negative counts


.. note::

    In addition, you can add, subtract, intersect and union Counters

    The unary add and sub will inplace remove pos or neg counts

----

OrderedDict
===========

* Pretty much a dictionary, but with order
* Equality also looks at the order
* Pretty straight forward

.. code:: python

    class OrderedCounter(Counter, OrderedDict):
        'Counter that remembers the order elements are first encountered'

        def __repr__(self):
            return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

        def __reduce__(self):
            return self.__class__, (OrderedDict(self),)


.. note::

    new in 3.1

    Return an instance of a dict subclass, supporting the usual dict methods.

    An OrderedDict is a dict that remembers the order that keys were first inserted.

    If a new entry overwrites an existing entry, the original insertion position is left unchanged.

    Deleting an entry and reinserting it will move it to the end.

    Order Matters for equality

----

defaultdict
===========

.. code:: python

    >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    >>> d = defaultdict(list)
    >>> for k, v in s:
    ...     d[k].append(v)
    ...
    >>> list(d.items())
    [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


.. note::
    
    Takes a callable to provide an initial value, hooks into the __missing__ that it adds to a standard dict

    The first argument provides the initial value for the default_factory attribute; it defaults to None.

    All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.

    This technique is simpler and faster than an equivalent technique using dict.setdefault()

----

User*
=====

* UserDict
* UserList
* UserString

.. note::

    These have all been supplanted by the ability to subclass directly from dict, list and str.

    Only big difference is that the underlying base data is stored in an attribute called `data`.

----

Go Out and Program, Mas!
========================

Credits and Links
+++++++++++++++++

* http://pymotw.com/2/collections/ -- Doug Hellmans' Most Excellent PyMOTW
* https://docs.python.org/3.4/library/collections.html -- Python Standard Library Docs
