#!/usr/bin/env python

# Program to print words that start with an uppercase letter
# example usage: cat test.txt | ./filterr

import fileinput
import string


for line in fileinput.input():
    words = line.split()
    for word in words:
        first_letter = ord(word[0])
        if first_letter >=65 and first_letter <=90:
            print word
