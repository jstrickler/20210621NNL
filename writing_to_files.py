with open('newfile.txt', 'w') as newfile_out:
    newfile_out.write("LINE 1\n")
    newfile_out.write("LINE 2\n")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open("fruits.txt", "w") as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

with open('DATA/alice.txt') as alice_in:
    with open('alice_lines.txt', 'w') as alice_out:
        with open('rabbit_lines.txt', 'w') as rabbit_out:
            for line in alice_in:
                if 'Alice' in line:
                    alice_out.write(line)
                if 'rabbit' in line.lower():
                    rabbit_out.write(line)
