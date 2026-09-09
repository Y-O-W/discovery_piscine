#!/usr/bin/env python3

import sys
import re

args = sys.argv[1:]

if len(args) == 2:
    pattern = args[0]
    arg = args[1]
    matches = re.findall(pattern, arg)
    count = len(matches)
    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")
