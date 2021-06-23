with open("../DATA/mary.txt") as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)


