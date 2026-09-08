#!/usr/bin/env python3

# TODO(human)
# Context: The exercise caps you at exactly two while loops to print all eleven multiplication tables (0–10) in the format Table of N: v0 v1 v2 ... v10.
# Your Task: In advanced_mult.py, replace TODO(human) with the full solution: an outer while loop over the table number (0 to 10) and an inner while loop over the multiplier (0 to 10) that builds and prints each line.
# Guidance: You'll need two counters that you reset/increment yourself (no range(), since this is while-loop practice). Think about whether it's easier to build the row as a growing string (e.g. start with f"Table of {n}:" and append f" {n*m}" each iteration) versus printing numbers one at a time with end=" " — either works, but note the exact spacing in the expected output (single space between the colon and the first number, and between each number).

table = 0

while table <= 10:
    line = f"Table of {table}:"
    mulitplier = 0
    while mulitplier <= 10:
        line += f" {table * mulitplier}"
        mulitplier += 1
    print(line)
    table += 1