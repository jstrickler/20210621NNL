#!/usr/bin/python3

ctemps = [ -40.2, 0.0, 37.938, 75.1889, 100.42371 ]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for c in ctemps:
    f = ((9 * c) / 5 ) + 32
    # print("{:.1f} C is {:.1f} F".format(c,f))
    print(f"{c:.1f} C is {f:.1f}")
print()

print("dirty:", fruits)
clean_fruits = [ f.strip().lower() for f in fruits ]
print("clean:", clean_fruits)

# print(', '.join(clean_fruits))
