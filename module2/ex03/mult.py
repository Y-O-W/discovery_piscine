#!/usr/bin/env python3

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
result = first_number * second_number

if result == 0:
    print(f"{first_number} x {second_number} = {result} \nThe result is positive and negative.")
elif result < 0:
    print(f"{first_number} x {second_number} = {result} \nThe result is negative.")
else:
    print(f"{first_number} x {second_number} = {result} \nThe result is positive.")
