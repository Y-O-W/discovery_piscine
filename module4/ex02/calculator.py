#!/usr/bin/env python3

first_number = int(input("Give me the first number: "))
second_number = int(input("Give me the second number: "))
addition = first_number + second_number
subtraction = first_number - second_number
division = first_number / second_number
multiplication = first_number * second_number

print(f"""Thank you!
    {first_number} + {second_number} = {addition}
    {first_number} - {second_number} = {subtraction}
    {first_number} / {second_number} = {division}
    {first_number} * {second_number} = {multiplication}""")
