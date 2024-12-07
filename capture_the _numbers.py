# using also regex,
# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.

import re

numbers = []
while True:
    try:
        line = input()
        if line:
            matches = re.findall(r'\d+', line)
            numbers.extend(matches)
    except EOFError:
        break

print(' '.join(numbers))
