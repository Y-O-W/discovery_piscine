#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(sys.argv) > 2:
    for arg in reversed(args):
        print(arg)
else:
    print("none")
