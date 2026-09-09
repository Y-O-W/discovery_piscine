#!/usr/bin/env python3

import sys

parameters = sys.argv[1:]

if len(parameters) > 0:
    count = len(parameters)
    print(f"parameters: {count}")
    for parameter in parameters:
        length = len(parameter)
        print(f"{parameter}: {length}")
else:
    print("none")
