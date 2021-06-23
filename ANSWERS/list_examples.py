list1 = list()  # new, empty list
print(list1)
list2 = [1, 2, 3]
print(list2)
list3 = ['a', 'b', 'c', 'mango']
print(list3)
list4 = []
print(list4)

cities = ['Pittsburgh', 'Albany', 'Colonie', 'Schenectady',
          "Homestead", 'McKeesport', 'Boston', 'Sewickley',
          'Troy']
print(cities, '\n')

cities.append('New York')
print(cities, '\n')
cities.append('Poughkeepsie')
print(cities, '\n')
cities.insert(0, 'Confluence')
cities.insert(4, 'Ohiopyle')
print(cities, '\n')

more_cities = ['Harrisburg', 'Elmira', 'Watkins Glen']

cities.extend(more_cities)
print(cities, '\n')

# junk = ['spam', 'ham']
# cities.append(junk)
# print(cities, '\n')
del cities[3]
print(cities, '\n')


# LIST.append(THING)       LIST + THING
# LIST.extend(THINGS)      LIST + THINGS[0] + THINGS[1] + THINGS[2] ...
# THINGS must be an *iterable*

cities.remove('Troy')
print(cities, '\n')

x = cities.pop()    # remove last element of list and return it
print("x is", x)
print(cities, '\n')

x = cities.pop(3)
print("x is", x)
print(cities, '\n')

cities[2] = 'Saratoga'
print(cities, '\n')

foods = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
print(foods.count('spam'))
print(foods.count('eggs'), '\n')

print(cities, '\n')
print(cities[0], cities[2], cities[11])
# print(cities[len(cities)-1])  # don't do this!
print(cities[-1])
cities[7] = "Oakmont"
print(cities, '\n')

#  LIST[start:stop:step]
print(cities[0:4], '\n')
print(cities[4:7])
print(cities[0:-1])
print(cities[1:-1])
print(cities[:5])  # [0:5]
print(cities[5:])
print(cities[-3:])
print(cities[5:1:-1])
print(reversed(cities[1:5]))  # saner

print(cities, '\n')

for city in cities:
    # city = <next element of> cities
    print(city)
print('-' * 60)

# for VAR in ITERABLE:
#     ...

letters = 'abc'
for letter in letters:
    print(letter)
print()

for fruit in 'apple', 'banana', 'mango':
    print(fruit.upper())
print()

for food in foods:
    if food != 'spam':
        print(food)
print()
