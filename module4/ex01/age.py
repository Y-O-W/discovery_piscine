#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
step = 10
years = step

print(f"You are currently {age} years old.")
while years <= 30:
    print(f"In {years} years, you'll be {years + age} years old.")  # placeholder math
    years += step
