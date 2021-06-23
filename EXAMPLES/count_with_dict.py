#!/usr/bin/python3

counts = {}
with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line.rstrip()
        if breakfast_item in counts:  # overwrite value
            counts[breakfast_item] = counts[breakfast_item] + 1
        else:  # add value
            counts[breakfast_item] = 1

for item, count in counts.items():
    print(item,count)
