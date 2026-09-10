#!/usr/bin/env python3

# Input

# Variable - Definition
class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
# Variable - Output

# Function - Definition
def average(items=None):
    if not items:
        return None
    else:
        return sum(items.values()) / len(items.values())

# Function - Call
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
print(f"no dictionary: {average()}.")
print(f"empty dictionary: {average({})}.")

# Function - Output
