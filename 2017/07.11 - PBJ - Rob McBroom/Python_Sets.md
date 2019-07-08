# Python Programming -- Sets

What you need to know.

.notes:Python also has an implementation of the mathematical set.  Unlike sequence objects such as lists and tuples, in which each element is indexed, a set is an unordered collection of objects.  Sets also cannot have duplicate members - a given object appears in a set 0 or 1 times.  For more information on sets, see the Set Theory wikibook. Sets also require that all members of the set be hashable. Any object that can be used as a dictionary key can be a set member. Integers, floating point numbers, tuples, and strings are hashable; dictionaries, lists, and other sets (except frozensets) are not.

---
# And what not to do

    !python
    keywordList = set(getKeywordList())
    refList = set(getReferenceList())
    retList = [r for r in refList]+[r for r in keywordList.difference(refList
    
---
# Constructing Sets

One way to construct sets is by passing any sequential object to the "set" constructor.

    !python
    >>> set([0, 1, 2, 3])
    set([0, 1, 2, 3])
    >>> set("obtuse")
    set(['b', 'e', 'o', 's', 'u', 't'])

We can also add elements to sets one by one, using the "add" function.

    !python
    >>> s = set([12, 26, 54])
    >>> s.add(32)
    >>> s
    set([32, 26, 12, 54])

---
Note that since a set does not contain duplicate elements, if we add one of the members of s to s again, the add function will have no effect.  This same behavior occurs in the "update" function, which adds a group of elements to a set.

    !python
    >>> s.update([26, 12, 9, 14])
    >>> s
    set([32, 9, 12, 14, 54, 26])

Note that you can give any type of sequential structure, or even another set, to the update function, regardless of what structure was used to initialize the set.

The set function also provides a copy constructor.  However, remember that the copy constructor will copy the set, but not the individual elements.

    !python
    >>> s2 = s.copy()
    >>> s2
    set([32, 9, 12, 14, 54, 26])

---
# Membership Testing

We can check if an object is in the set using the same "in" operator as with sequential data types.

    !python
    >>> 32 in s
    True
    >>> 6 in s
    False
    >>> 6 not in s
    True

We can also test the membership of entire sets.  Given two sets S_1 and S_2, we check if S_1 is a Subset or a superset of S_2.

    !python
    >>> s.issubset(set([32, 8, 9, 12, 14, -4, 54, 26, 19]))
    True
    >>> s.issuperset(set([9, 12]))
    True

Note that "issubset" and "issuperset" can also accept sequential data types as arguments

---
    !python
    >>> s.issuperset([32, 9])
    True

Note that the <= and >= operators also express the issubset and issuperset functions respectively.

    !python
    >>> set([4, 5, 7]) <= set([4, 5, 7, 9])
    True
    >>> set([9, 12, 15]) >= set([9, 12])
    True

Like lists, tuples, and string, we can use the "len" function to find the number of items in a set.

---
# Removing Items

There are three functions which remove individual items from a set, called pop, remove, and discard.  The first, pop, simply removes an item from the set.  Note that there is no defined behavior as to which element it chooses to remove.

    !python
    >>> s = set([1,2,3,4,5,6])
    >>> s.pop()
    1
    >>> s
    set([2,3,4,5,6])

We also have the "remove" function to remove a specified element.

    !python
    >>> s.remove(3)
    >>> s
    set([2,4,5,6])

---
However, removing a item which isn't in the set causes an error.

    !python
    >>> s.remove(9)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    KeyError: 9

If you wish to avoid this error, use "discard."  It has the same functionality as remove, but will simply do nothing if the element isn't in the set

We also have another operation for removing elements from a set, clear, which simply removes all elements from the set.

    !python
    >>> s.clear()
    >>> s
    set([])

---
# Iteration Over Sets

We can also have a loop move over each of the items in a set.  However, since sets are unordered, it is undefined which order the iteration will follow.

    !python
    >>> s = set("blerg")
    >>> for n in s:
    ...     print n,
    ...
    r b e l g

---
# Set Operations

.notes:Python allows us to perform all the standard mathematical set operations, using members of set.  Note that each of these set operations has several forms.  One of these forms, s1.function(s2) will return another set which is created by "function" applied to S_1 and S_2.  The other form, s1.function_update(s2), will change S_1 to be the set created by "function" of S_1 and S_2.  Finally, some functions have equivalent special operators.  For example, s1 & s2 is equivalent to s1.intersection(s2)

---
# Union

The union is the merger of two sets.  Any element in S_1 or S_2 will appear in their union.

    !python
    >>> s1 = set([4, 6, 9])
    >>> s2 = set([1, 6, 8])
    >>> s1.union(s2)
    set([1, 4, 6, 8, 9])
    >>> s1 | s2
    set([1, 4, 6, 8, 9])

Note that union's update function is simply "update".

---
# Intersection

Any element which is in both S_1 and S_2 will appear in their intersection.

    !python
    >>> s1 = set([4, 6, 9])
    >>> s2 = set([1, 6, 8])
    >>> s1.intersection(s2)
    set([6])
    >>> s1 & s2
    set([6])
    >>> s1.intersection_update(s2)
    >>> s1
    set([6])

---
# Symmetric Difference

The symmetric difference of two sets is the set of elements which are in one of either set, but not in both.

    !python
    >>> s1 = set([4, 6, 9])
    >>> s2 = set([1, 6, 8])
    >>> s1.symmetric_difference(s2)
    set([8, 1, 4, 9])
    >>> s1 ^ s2
    set([8, 1, 4, 9])
    >>> s1.symmetric_difference_update(s2)
    >>> s1
    set([8, 1, 4, 9])

---
# Set Difference

Python can also find the set difference of S_1 and S_2, which is the elements that are in S_1 but not in S_2.

    !python
    >>> s1 = set([4, 6, 9])
    >>> s2 = set([1, 6, 8])
    >>> s1.difference(s2)
    set([9, 4])
    >>> s1 - s2
    set([9, 4])
    >>> s1.difference_update(s2)
    >>> s1
    set([9, 4])

---
# Multiple sets
Starting with Python 2.6, "union", "intersection", and "difference" can work with multiple input by using the set constructor. For example, using "set.intersection()":

    !python
    >>> s1 = set([3, 6, 7, 9])
    >>> s2 = set([6, 7, 9, 10])
    >>> s3 = set([7, 9, 10, 11])
    >>> set.intersection(s1, s2, s3)
    set([9, 7])

---
# frozenset
A frozenset is basically the same as a set, except that it is immutable - once it is created, its members cannot be changed. Since they are immutable, they are also hashable, which means that frozensets can be used as members in other sets and as dictionary keys. frozensets have the same functions as normal sets, except none of the functions that change the contents (update, remove, pop, etc.) are available.

    !python
    >>> fs = frozenset([2, 3, 4])
    >>> s1 = set([fs, 4, 5, 6])
    >>> s1
    set([4, frozenset([2, 3, 4]), 6, 5])
    >>> fs.intersection(s1)
    frozenset([4])
    >>> fs.add(6)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'frozenset' object has no attribute 'add'

---
# Reference

[Python Set Reference](http://docs.python.org/library/stdtypes.html#set-types-set-frozenset Python Library Reference on Set Types)

# Credits

Python Programming Wikibook

<http://en.wikibooks.org/wiki/Python_Programming/Sets>

Text is available under the [Creative Commons Attribution-ShareAlike License](http://en.wikibooks.org/wiki/Wikibooks:Creative_Commons_Attribution-ShareAlike_3.0_Unported_License).

