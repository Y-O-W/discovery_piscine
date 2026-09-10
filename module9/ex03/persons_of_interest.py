#!/usr/bin/env python3

# Input

# Variable - Definition
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

other = {"marie": {"name": "Marie Curie", "date_of_birth": "1867"}}

# Variable - Output

# Function - Definition
def famous_births(items=None):
    if not items:
        return None
    else:
        ordered = sorted(items.values(), key=lambda person: person["date_of_birth"])
        for person in ordered:
            print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# Function - Call
famous_births(women_scientists)
famous_births(other)

# Function - Output
