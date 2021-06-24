file_name = "wombats.txt"
with open(file_name) as wombats_in:
    for line in wombats_in:
        print(line.rstrip())

colors = ['red', 'blue', 'green', 'orange']
print(colors[9])

values = 5, 8.1, 0.0, 4.3, 2.7
for v in values:
    result = 23 / v
    print(result)

