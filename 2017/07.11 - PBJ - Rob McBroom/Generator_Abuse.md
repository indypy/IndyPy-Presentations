# Generator Abuse #

Rob McBroom

* * * * * * * * * *

## Basic Generator ##

    !python
    def gen1():
        for x in ('Garnet', 'Violet', 'Ruby'):
            yield x

* * * * * * * * * *

## Multiple `yeild` Statements ##

    !python
    def gen2():
        yield "Start"
        for x in ('Garnet', 'Violet', 'Ruby'):
            yield x
        yield "Finish"

* * * * * * * * * *

## Postponing Expensive Operations ##

    !python
    from time import sleep
    
    
    def fun3():
        sleep(2.0)
        return (4, 5, 6)


    def gen3():
        sleep(2.0)
        for x in (4, 5, 6):
            yield x

  * Defining Roles in Fabric

* * * * * * * * * *

## Multiple Background Tasks ##

    !python
    from time import time
    from collections import deque
    
    
    def gen4(delay=3.0):
        stop_time = time() + delay
        while True:
            if time() < stop_time:
                yield None
            else:
                yield "Results after {}s".format(delay)
    
    # continued…

* * * * * * * * * *

## Multiple Background Tasks ##

    !python
    tasks = deque()
    for delay in (1.0, 4.0, 3.0, 3.0, 1.5):
        t = gen4(delay)
        tasks.append(t)
    
    while tasks:
        task = tasks.popleft()
        try:
            result = task.next()
            if result is None:
                tasks.append(task)
            else:
                print result
        except StopIteration:
            pass

* * * * * * * * * *

## Links ##

<http://www.dabeaz.com/generators/>
