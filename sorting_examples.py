fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava", 
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon", 
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

# str.lower(x)

f2 = sorted(fruits, key=str.lower)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def ignore_case(f):
    return f.lower()

f4 = sorted(fruits, key=ignore_case)
print("f4: {}\n".format(f4))

def my_custom(f):
    return len(f), f.lower()

f5 = sorted(fruits, key=my_custom)
print("f5: {}\n".format(f5))

def wacky(x):
    return x[-1]

f6 = sorted(fruits, key=wacky)
print("f6: {}\n".format(f6))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(sorted(nums), '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print()

def by_dob(p):
    return p[3]

for person in sorted(people, key=by_dob):
    print(person)
print()

print("Using lambda:")
for person in sorted(people, key=lambda p: p[1]):
    print(person)
print()

# lambda param: return-value

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(list(airports.items()), '\n')

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(element):
    return element[1], element[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()

print("Lambda version:")
for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)
print()

n1 = sorted(nums)
print("n1: {}\n".format(n1))

n2 = sorted(nums, reverse=True)
print("n2: {}\n".format(n2))

f7 = sorted(fruits, key=str.lower, reverse=True)
print("f7: {}\n".format(f7))

print(nums)
nums.sort()
print(nums)













