#!/usr/bin/env python3

import sys
import re

parameters = sys.argv[1:]

if len(parameters) == 1:
    word = parameters[0]
    character = "z"
    matches = re.findall(character, word)
    if len(matches) > 0:
            print(f"{"".join(matches)}")
    else:
        print("none")
else:
    print("none")
