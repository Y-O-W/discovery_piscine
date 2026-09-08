#!/usr/bin/env python3

import sys

parameters = 0

if len(sys.argv) > 1:
    parameters = len(sys.argv) - 1
    print("Got arguments")

print(f"Number of parameters: {parameters}.")