#!/usr/bin/env python3

original_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []

for i in range(len(original_list)):
    if original_list[i] > 5:
        new = original_list[i] + 2
        new_list.append(new)

print(f"""Original List: {original_list}
    New List: {new_list}""")
