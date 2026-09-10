#!/usr/bin/env python3

import sys

parameters = sys.argv[1:]

# Function - Definition

def shrink(word=""):
    new_word = word[:8]
    print(new_word)

def enlarge(word=""):
    new_word = word
    while len(new_word) != 8:
        new_word += "Z"
    print(new_word)

# Function - Call
if len(parameters) > 0:
    for parameter in parameters:
        if len(parameter) > 8:
            shrink(parameter)
        elif len(parameter) < 8:
            enlarge(parameter)
        else:
            print(parameter)
else:
    print("none")
