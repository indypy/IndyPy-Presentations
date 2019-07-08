# Python Iterators and Generators

---
# Python Iterators

---
## What are Iterators?

* A protocol that many Python objects implement
* A General Pattern to allow easy traversal of a container
* Since Python 2.2 they are now a fundamental part of the language

.notes: The underlying structure of the containers storage doesn't need to be exposed and can be easily changed

.notes: Works very similar to a database cursor.

---
## In Python

* Implicitly used for `for` loops, list comprehensions and generator statements
* All standard built-in collections types support iteration

---
## Quick Example

Implicit usage:

    !python
    for value in squence:
        print value


---
## Useful example

Reading from a file:

    !python
    datafile = open('datafile')
    for line in datafile:
        do_something(line)

.notes: uses the built-in iterator of the file object

---
## More Examples

Here we use a `try` and an `except` to control the flow

    !python
    it = iter(sequence)
    while True:
        try:
            value = it.next() # in Python 2.x
        except StopIteration:
            break
        it = iter(it)
        print value

.notes: `iter()` built-in is used to return a iterator object.

.notes: This example is just more explicit with the definition of the iterable.


---
## List Comprehensions

* These ROCK
* Use them to make your code more consise and clear
* Do not use them to introduce magically small blocks of code

---
## List Comprehension

Before:

    !python
    >>> squares = []
    >>> for x in range(10):
    ...     squares.append(x**2)
    ...
    >>> squares
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]]

After:

    !python
    >>> squares = [x**2 for x in range(10)]

.notes: This is also eqivelent to `squares = map(lambda x: x**2, range(10))` but quite a bit more readable, and readibilty counts!

---
## List Comprehension

    !python
    >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]]

.notes: The `for` portion always comes before the `if` portion.

.notes: The `if` statement is evaluated in the context of the `for` loop it is in.

---
## DIY Iterators

Create a class that implements just one method:

    !python
    container.__iter__()

This returns an iterator object which implements:

    !python
    iterator.__iter__()

    iterator.next()

When the container is out of items, raise `StopIteration`

.notes: the `__iter__()` is required to support `for` and `in` statements in Python.

.notes: the `iterator.next()` will pass back the next item from the container until you raise `StopIteration`.

---
# Python Generators

---
## What are Generators?

* Convenient way to implement the `iterator` protocol
* It is a function that returns an `iterator`
* Implement the `container.__iter__()` as a generator
* Looks like a normal function, but contains a `yield` statement

.notes: Generator functions will proceed until a `yield` and then suspend execuction of the generator function. All local state is retained including current bindings of local variables, the instruction pointer and the internal evaluation stack.

.notes: Generator functions will proceed on the next call of the generator's methods.

---
## Generator Example

Without Generators:

    !python
    # Build and return a list
    def firstn(n):
        num, nums = 0, []
        while num < n:
            nums.append(num)
            num += 1
        return nums

    sum_of_first_n = sum(firstn(1000000))

.notes: straight forward, but it builds the list in memory and will keep all `n` "10 MB" integers in memory.

---
## Generator Exmaple

With generator pattern (using iterators):

    !python
    # Using the generator pattern (an iterable)
    class firstn(object):
        def __init__(self, n):
            self.n = n
            self.num, self.nums = 0, []

        def __iter__(self):
            return self

        def next(self):
            if self.num < self.n:
                cur, self.num = self.num, self.num+1
                return cur
            else:
                raise StopIteration()

    sum_of_first_n = sum(firstn(1000000))

.notes: Lot's of boilerplate going on here

---
## Generator Exmaple

With a generator function:

    !python
    # a generator that yields items instead of returning a list
    def firstn(n):
        num = 0
        while num < n:
            yield num
            num += 1

    sum_of_first_n = sum(firstn(1000000))

.notes: Much more readable and only needs values on demand so uses very little memory. In this example, `firstn()` is equivilent to the python built-in `xrange()`.

---
## Generator Expressions

Similar to a list comprension, but `yeilds` results to be more efficient

    !python
    >>> sum(i*i for i in range(10)) # sum of squares 0,1,4, ... 81)
    285

---
## Resources

* https://en.wikipedia.org/wiki/Iterator
* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#generators
* http://docs.python.org/2/library/stdtypes.html#iterator-types
* http://docs.python.org/2/reference/expressions.html#yieldexpr
* http://wiki.python.org/moin/Generators
* http://rgruet.free.fr/PQR27/PQR2.7.html
