#!/usr/bin/env python3

import sys

parameters = sys.argv[1:]

# Function - Definition
def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        message = f"Hello, {name}."
        print(message)

# Function - Call
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
