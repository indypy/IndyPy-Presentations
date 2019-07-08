theme: Ostrich, 2
autoscale: true
slidenumbers: true
slidecount: true
footer: IndyPy September 2017 PBJ

[.slidenumbers: false ]
[.footer: ]
![fit](indypy_logo.png)
### **IndyPy** September 2017 PBJ

# [fit] List Comprehensions

# :snake:

#### Calvin Hendryx-Parker
#### [Six Feet Up](http://www.sixfeetup.com)

---
![](https://c1.staticflickr.com/3/2475/3559426073_067a8f2665_b.jpg)

# What is a
# [fit] List Comprehension?

^ Converting one list (or any iterator) into a another list

^ How do you normally convert from one list to another?  With a loop!

^ https://www.flickr.com/photos/martinko/3559426073/

---

# Common Loops

```python
some_existing_list = [1,2,3,4]

shiny_new_list = []
for n in some_existing_list:
    if conditionally_include(n):
        shiny_new_list.append(n * 2)
```

---
![](https://c2.staticflickr.com/4/3188/2354086423_7cdb6043d8_b.jpg)

# [fit] Readability Counts.

^ https://www.flickr.com/photos/thomashawk/2354086423/

---
![](https://c1.staticflickr.com/7/6178/6250429946_30b58ab48c_b.jpg)

# Copy and Paste
## Your Way to Readability

^ Credit to Trey Hunner

^ https://www.flickr.com/photos/mrbd/6250429946

---

```python, [.highlight: 3]
some_existing_list = [1,2,3,4]

shiny_new_list = []
for n in some_existing_list:
    if conditionally_include(n):
        shiny_new_list.append(n * 2)
```

### Our List Comprehension

```python
shiny_new_list = []
```

---

```python, [.highlight: 6]
some_existing_list = [1,2,3,4]

shiny_new_list = []
for n in some_existing_list:
    if conditionally_include(n):
        shiny_new_list.append(n * 2)
```

### Our List Comprehension

```python
shiny_new_list = [n * 2]
```

---

```python, [.highlight: 4]
some_existing_list = [1,2,3,4]

shiny_new_list = []
for n in some_existing_list:
    if conditionally_include(n):
        shiny_new_list.append(n * 2)
```

### Our List Comprehension

```python
shiny_new_list = [n * 2 for n in some_existing_list]
```

---

```python, [.highlight: 5]
some_existing_list = [1,2,3,4]

shiny_new_list = []
for n in some_existing_list:
    if conditionally_include(n):
        shiny_new_list.append(n * 2)
```

### Our List Comprehension

```python
shiny_new_list = [n * 2 for n in some_existing_list if conditionally_include(n)]
```

---

### Our List Comprehension

```python
shiny_new_list = [n * 2 for n in some_existing_list if conditionally_include(n)]
```

#### Could be

```python
shiny_new_list = [n * 2 for n in some_existing_list]
```

#### If you don't need the conditional

---

# Nested List Comprehensions

```python
nested = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

### Is the equivalent of:

```python
nested = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            nested.append((x, y))
```

^ Note how the order of the for and if statements is the same in both these snippets.

---

# Other Comprehensions

* Sets
* Dictionary

---
[.build-lists: true]

# Set Comprehension

```python
a = {x for x in 'abracadabra' if x not in 'abc'}
```

* `a = {'r', 'd'}`

---
[.build-lists: true]

# Dictionary Comprehension

## Similar, but has a colon, like a `dict`

```python
b = {x: x**2 for x in (2, 4, 6)}
```

* `b = {2: 4, 4: 16, 6: 36}`

---
![](https://c1.staticflickr.com/9/8670/16648403629_c2c30a4781_b.jpg)

# Resources

* [Python List Comp Docs](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Trey Hunner's Blog on List Comps](http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)

^ https://www.flickr.com/photos/davidjthomas/16648403629
