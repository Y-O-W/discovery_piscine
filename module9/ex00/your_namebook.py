#!/usr/bin/env python3

# Input

# Variable - Definition
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
# Variable - Output

# Function - Definition
def array_of_names(persons):
    return [f"{first.capitalize()} {last.capitalize()}" for first, last in persons.items()]

# Function - Call
print(array_of_names(persons))

# Output
# print(persons)
