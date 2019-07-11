# “Extracting Readable Output from Data Structures in Python Using Pretty Printing Modules”
## Author: Eileen Tallman
Github Profile: https://github.com/etallman
Original Repo: https://github.com/etallman/pretty_printing_modules
### Presented at IndyPy: Favorite Tools, Indianapolis, IN, July 9, 2019.



#Running Code Examples
Prior to running code examples, please be sure to pip install modules.

PprintPP:
https://pypi.org/project/pprintpp/
pip install pprintpp

Texttable:
https://pypi.org/project/texttable/
pip install texttable

pip install tabulate
https://pypi.org/project/tabulate/

pip install ptable
https://pypi.org/project/PTable/


# INTRODUCTION

Novice Python coders may be unaware about some of the built-in or easily accessible modules that could help them print data structures in a readable format. Early in the learning process, coders may be likely to rely on string and list functions on which they are more familiar, for example, .join() or .format().

This talk will briefly review my favorite Python pretty printing modules,  pprint, texttable, tabulate, and ptable, for displaying small data structures. Each of these modules will be demonstrated with code examples.

#PPRINT AND PRETTY PRINTER

## What Does it Do?
<ul>
<li>The pprint, or "pretty print" module makes output from Python data structures more readable. This output can be used as input to the interpreter.</li>
<li>Pprint tries to return output on a single line if it can, and breaks them onto multiple lines with indentation if it doesn't fit width constraints.</li>
<li>Adopts sys.stdout and is a part of the standard library.</li>
</ul>
## Customizaton

The module allows for some customization using INDENT, DEPTH, and WIDTH.
<li> INDENT -- can control for the amount of indentation on each line.</li>
<li>DEPTH -- allows you to specify the levels deep in your code to print.</li>
<li>WIDTH -- allows you to adjust maximum characters on display per line.</li>

Here is an example of pprint in a list context.
(See Example 1 in pprint_examples.py)

And next I've displayed a nested tuple. Notice the primary difference is the ability to choose the level of tuple that is printed by selecting the depth customization.
(See Example 2 in pprint_examples.py)

## Using Pprint in an API Call
(See Example 3 in pprint_examples.py)

## Pretty Printer Derivative Functions
PPrint module has one PrettyPrinter class which supports derivative functions.
[Table](https://docs.google.com/document/d/1Nr9sLQLF51r6_reRT6AJp0AevdE37ycDKgftJrhQMrE/edit?usp=sharing)

Derivative Functions, like pformat, can be combined with the logging module.
(See Example 4 in pprint_examples.py)

# PPrintPP
PPrintpp is a module that requires a pip install. It is similar to Pprint, but the advantage is that it is Pep8 compliant.
(See Example 5 in pprint_examples.py)

## Limitations
<ol>
<li>Pprint is easily accessible, but it is limited to basic data structures. Other structures such as files or sockets may not work will in pprint. </li>
<li>Pprint is also pretty limited in its formatting. If we wanted to view data sets in a more readable format, for example, in a table format, we would want to use some different modules.</li>
  </ol>


# Texttable

## What Does it Do?
<ul>
<li>It creates simple, formatted ASCII tables that may include a header, title, and columns and rows drawn using a specific character as the border.</li>
<li>Texttable allows for limited customization, such as column and row alignment and even colorization. It is easy to use when creating a small data set.</li>
<li>It supports fixed-size tables, where column sizes are pre-determined, for reading and writing (including with a dictionary).</li>
<li>Texttable also supports dynamic-sized tables, where column width is deduced to be the largest element in the column, for writing only.</li>
</li>

(See Examples 6 and 7 in texttable_examples.py)

## Limitations
<ol>
  <li>Enforces some rigid rules to the tables. For example,  cells may not span multiple rows or columns and corners must all be identical, including in the header and all borders. </li>
    <li>This module only parses text tables. It will not assist in parsing HTML, LaTeX, or any other kind of markup.</li>
  </ol>


# Tabulate

## What Does it Do?
<ul>
  <li>Presents a formatted, fixed-width table for pretty printing.</li>
  <li>There's no need to do custom settings and format every time you add new item to the list.</li>
  <li>Tabulate has several preset table formats: </li>
<ul>
  <li>plain</li>
  <li>simple</li>
  <li>grid</li>
  <li>fancy_grid</li>
  <li>psql</li>
  <li>pipe</li>
      <li>orgtbl</li>
  <li>rst</li>
  <li>mediawiki</li>
  <li>etc..</li>
  </ul>
<li>It tries to detect column types automatically, and aligns the values by decimal points as a default. These can be overriden by setting the alignment manually</li>
 <li>Multiline cells are supported by the formats without row delimiters (i.e., plain or simple)</li>
  <li>Per tabulate documentation, given a 10x10 table (a list of lists) of mixed text and numeric data, tabulate is faster than PrettyTable and texttable.</li>
 </ul>
 (See Examples 8 and 9 in tabulate_examples.py)

 ## Limitations
<ol>
  <li>Per tabulate documentation, given a 10x10 table (a list of lists) of mixed text and numeric data, tabulate is slower than asciitable.</li>
<li>Because tabulate has decimal point alignment and parses everything as a number, it has some features that can be limiting:</li>
  <ul>
   <li>Has to "guess" how to print a particular tabular data type.</li>
  <li>Needs to keep the entire table in-memory</li>
  <li>Has to "transpose" the table twice</li>
  <li>Does much more work than it may appear</li>
  </ul>
<li>May not be good to use for large tables.</li>
  <li>May not be good for performance-sensitive conditions (is tabout two orders of magnitude slower than simply joining lists of values with a tab, coma or other separator.)</li>
  </ol>

# PTable
## What Does it Do?
<ul>
<li>PTable offers a quick way to represent tabular data in stylized ASCII tables. It offers a variety of formatting options such as border, headers, padding, etc. </li>
<li>Styles can be changed all at once or as individual lines. </li>
<li>PTable can read data from a csv, html, or database (sql)</li>
<li>PTable can write data in ASCII or HTML.</li>
</ul>

## Data Manipulation
Using PTable will allow you to select a subset of data for viewing, change column alignment, or even sort your data.
(See Example 10 in ptable_examples.py)

Here is an example of data sorted by Population:
(See Example 11 in ptable_examples.py)

## Limitations
<ol>
<li>PTable performs more slowly than tabulate or modules that have more limited functionality.</li>
  <li>PTable is currently only compatible with Python versions up to 3.0.</li>
</ol>

## Conclusion
Thank you for letting me review my favorite Python pretty printing modules with you today! Hopefully this talk will help other Python beginners save time and produce better looking output.
