#!/usr/bin/env python
import re

with open('../DATA/lorem.txt') as lorem_in:
    s = lorem_in.read()

#       upper case letter, '-',  2 or 3 digits
pattern = r'[A-Z]-\d{2,3}'  # <1>

if re.search(pattern, s):  # <2>
    print("Found pattern.")
print()

m = re.search(pattern, s)  # <3>
print(m)
if m:
    print("Found:", m.group(0), m.start(0), m.end(0))  # or, m.group()
    print(s[m.start():m.end()])
print()

for m in re.finditer(pattern, s):  # <5>
    print(m.group())  # or m.group(0)
print()

# matches = [m.group() for m in re.finditer(pattern, s)]
matches = re.findall(pattern, s)  # <6>
print("matches:", matches)
