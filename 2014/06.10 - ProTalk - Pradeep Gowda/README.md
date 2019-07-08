---
title: iPython
author: Pradeep Gowda <pradeep@btbytes.com>
date: Tuesday, June 10 2014
---



## The Python interpreter

- Simple calculator
- Try out snippets of code
- Play with data files
- `help(os)`
- `dir(os)`


## What is iPython

iPython = `interactive` python

- Interactive shell (duh!)
  - tab completion
  - object introspection
  - better tracebacks
  - syntax shortcuts
  - autoindent
  - history management
  - output caching
- GUI support - Qt, (`%gui`)
- Browser based "notebook"
- data visualisation
- OS integration
   - `!echo "hello shell"`
   - `foo = !dosomething.sh`
- software development
  - `%run`
  - `%timeit`
  - `%debug`
  - `%prun`
- ~~embeddable interpreters~~
- ~~parallel computing~~

~[architecture](images/interactive.png)

In summary:

    iPython = Python Shell + OS access + GUI + more
              + Protocol (ZMQ)
              + Notebook (Web) for collaboration
              + Parallel computing


The goals of iPython are over-arching. But, you can benefit from
iPython even if you don't have use for many of it's "scientific
computing/datascience" aspects.



## Installation

    mkvirtualenv indypy
    pip install ipython

If you want the notebook interface:

    $install tornado #python async framework
    $install pyside #python bindings for Qt (F/OSS)
    $install pyzmq
    $install matplotlib #for pretty graphics



## Now for something completely different: anaconda

The easy, sane and complete option: use **anaconda** distribution by
`continuum.io`.

    http://docs.continuum.io/anaconda/

> Anaconda is a free collection of powerful packages for Python that
> enables large-scale data management, analysis, and visualization for
> Business Intelligence, Scientific Analysis, Engineering, Machine
> Learning, and more.


Use the `conda` tool for managing environments and packages.

![conda update](images/conda-conda.png)

Remember: You don't need to use the `anaconda` distribution if all you want
is the `iPython` REPL.


## Demo


Object details: `?`

    import os
    os?

    Type:       module
    String Form:<module 'os' from '/Users/pradeep/anaconda/python.app/Contents/lib/python2.7/os.pyc'>
    File:       /Users/pradeep/anaconda/python.app/Contents/lib/python2.7/os.py
    Docstring:
    OS routines for Mac, NT, or Posix depending on what system we're on.

    This exports:
    - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
    - os.path is one of the modules posixpath, or ntpath
    ...
    ...

More information: `??`

    os??


### Logging your session: `%logstart`

How to use it tho?

    %logstart?

From the shell:

    ipython -i session_log.py

### Magic commands: `%`

Commands starting with `%` are called magic commands.

    %pastebin hello.py

Commands starting with `%` are called magic commands. You can define
your own.  You can define your own custom magic commands.



### History

    # all of history
    %history

    # only a few
    %history 5-9

    #specific
    %history 5 9

    # save them to a file
    %save test1.py 5-9

    #access the history objects
    In?
    Out?

    _
    __

    print In[1]
    Out

## Load python code: `%load`

    %load fact.py

## Timeit: %timeit

    %timeit factorial(10)


### Run python code: `run hello`

    run hello
    ..error...

### OS/shell integration

    ls
    files = !ls
    files
    files.s
    files.n
    files.p

Shell integration: `!`

    !pandoc
    #hello
    this is a simple document
    ^d
    <h1 id="hello">hello</h1>
    <p>this is a simple document</p>


### QtConsole

    $ipython qtconsole


### Notebook

    $ipython notebook --pylab --ip=*

You can now connect from another machine on the network.

![Keyboard shortcuts](images/notebook-kbd.png)

Demo of ipython notebook

Loading some one else's notebook

- drag and drop the file on the web page


### [iPython Extensions](http://ipython.org/ipython-doc/2/config/extensions/index.html)

Bundled:

    autoreload
    cythonmagic
    octavemagic
    rmagic
    storemagic
    sympyprinting


Interesting:

    sql

#### `ipython-sql`

[iPython-sql](https://pypi.python.org/pypi/ipython-sql) Introduces a `%sql` (or `%%sql`) magic.

Connect to a database, using SQLAlchemy connect strings, then issue
SQL commands within IPython or IPython Notebook.


    pip install ipython-sql
    pip install psycopg2
    %load_ext sql
    %%sql postgresql://pradeep:kishore@localhost/dvdrental
    select * from actor limit 10;

![SQL result](images/sql.png)



### [Display](http://goo.gl/ym1nBp)

    from IPython.display import Image
    Image(url='http://i.imgur.com/eF8kh6w.gif')


How is iPython notebook used?

- Visualization: <http://nbviewer.ipython.org/gist/cparmer/7628933>
- Graphics using Asymptote: <http://goo.gl/IaU6Ov>
- Using R from with iPython: <http://goo.gl/or1kkR>
- Haskell programming with iPython: <http://gibiansky.github.io/IHaskell/demo.html>
- How about dynamic web viz? <http://goo.gl/D5vHRS>
- Interactive web widgets: <http://jakevdp.github.io/blog/2013/12/05/static-interactive-widgets/>
- Economics: <http://nbviewer.ipython.org/url/norvig.com/ipython/Economics.ipynb>
- Teaching:
    - <http://www.kevinsheppard.com/Python_for_Econometrics>
    - <http://www.kevinsheppard.com/Python_Course>
- **[A gallery of interesting iPython notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)**

## Windows

What if I live inside Visual studio?

- Python Tools for Visual Studio -- http://goo.gl/qJXQEp
