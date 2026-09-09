#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) == 1:
    word = args[0]
    ask = input("What was the parameter? ")
    if word == ask:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
