#!/usr/bin/env python3

# Input
import sys
parameters = sys.argv[1:]

# Variable - Definition
start = 10
print(start)

# Function - Definition
def add_one(num=0):
    new_num = num
    new_num += 1
    print(new_num)

# Function - Call
add_one(start)

# Output
print(start)
