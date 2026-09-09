#!/usr/bin/env python3

import sys

parameters = sys.argv[1:]

# Definition - Function
def downcase_it(string):
    new_string = string.lower()
    return new_string

if len(parameters) > 0:
    for parameter in parameters:
        print(downcase_it(parameter))
else:
    print("none")
