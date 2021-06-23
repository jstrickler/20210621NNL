# file_obj = open(file_name, file_mode)
# file_obj.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    file_contents = mary_in.read()  # read entire file into var
    print("RAW:")
    print(repr(file_contents))
    print("NORMAL:")
    print(file_contents)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)




