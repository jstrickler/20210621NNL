fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava"]

f0 = []
for last_names in fruits:
    f0.append(last_names.upper())
print("f0:", f0, '\n')

#    [EXPR  for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [len(f) for f in fruits]
print(f"f2: {f2}\n")

f3 = [f.upper() for f in fruits if f.startswith('a')]
print(f"f3: {f3}\n")

f4 = [f for f in fruits if f.startswith('a')]
print(f"f4: {f4}\n")

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

m = []
for p in people:
    print(f"p: {p} p[1]: {p[1]}")
    m.append(p[1])
print()
print("m:", m, '\n')

last_names = [p[1] for p in people]
print(f"last_names: {last_names}\n")

last_names_gen = (p[1] for p in people)
print(last_names_gen)
for last_name in last_names_gen:
    print(last_name)

