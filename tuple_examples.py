
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(person, type(person))

print(person[0], person[1])

x = ['do', 're', 'mi']
a, b, c = x

first_name, last_name, product, dob = person
# first_name = person[0]
# last_name = person[1]
# ...

print(first_name, last_name)

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
print(type(people))
print(type(people[0]))
print(type(people[0][0]), '\n')

for person in people:
    print(person[0], person[1])
print('-' * 60)

for person in people:
    first_name, last_name, product, dob = person
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product, dob in people:
    # var, var, ... = <next element of> people
    print(first_name, last_name)
print('-' * 60)

cities = [('Ohiopyle', 'PA'), ('Elmira', 'NY'),
          ('Durham', 'NC'), ('Plano', 'TX')]

for city, state in cities:
    print(city, state)
print()



