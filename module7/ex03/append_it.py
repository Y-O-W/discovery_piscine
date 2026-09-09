#!/usr/bin/env python3

import sys

parameters = sys.argv[1:]

if len(parameters) > 0:
    for parameter in parameters:
        if parameter.find("ism") != len(parameter) - len("ism"):
            parameter += "ism"
            print(f"{parameter}")
        # if not parameter.endswith("ism"): --> alternative method
        #    print(parameter + "ism")
else:
    print("none")
