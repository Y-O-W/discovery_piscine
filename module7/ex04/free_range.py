#!/usr/bin/env python3

import sys

# parameters = sys.argv[1:]
parameters = [int(arg) for arg in sys.argv[1:]] # list comprehension

if len(parameters) == 2 and int(parameters[0]) < int(parameters[1]):
    print(list(range(parameters[0], parameters[1] + 1)))
else:
    print("none")
