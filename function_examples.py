
def half(x):
    return x / 2

a = half(10)
print("a: {}\n".format(a))

m = 28.93023
print(half(m))

def hello():
    print("Hello Knowles and Bettis world")

hello()
x = hello()
print("x: {}\n".format(x))

def find_words(word, file_name):
    lines = []
    with open(file_name) as file_in:
        for line in file_in:
            if word in line:
                lines.append(line.rstrip())
    return lines

results = find_words('lamb', 'DATA/mary.txt')
print(results)

print(find_words('bird', 'DATA/parrot.txt'))


