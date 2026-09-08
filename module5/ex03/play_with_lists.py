#!/usr/bin/env python3

original_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = set()

for i in range(len(original_list)):
    if original_list[i] > 5:
        new = original_list[i] + 2
        new_list.add(new)

print(f"""{original_list}
    {new_list}""")
