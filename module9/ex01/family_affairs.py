#!/usr/bin/env python3

# Input

# Variable - Definition
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
# Variable - Output

# Function - Definition
def find_the_redheads(dupont_family):
    return list(filter(lambda name: dupont_family[name] == "red", dupont_family.keys()))

# Function - Call
print(find_the_redheads(dupont_family))

# Output
