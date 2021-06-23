
x = ['e', 'd', 'a', 'c', 'b']

print(len(x), min(x), max(x), sorted(x))

m = [99, 8, 57, 3, -10, 5.6, 9, 2.1]
print(len(m), min(m), max(m), sorted(m), sum(m))

s = 'wombat'
print(len(s), min(s), max(s), sorted(s))

t = 8, "abc", 99
print(len(s))

cities = ['Pittsburgh', 'Albany', 'Colonie', 'Schenectady',
          "Homestead", 'McKeesport', 'Boston', 'Sewickley',
          'Troy']

print(sorted(cities), '\n')

rev_cities = reversed(cities)
print(rev_cities, '\n')
# print(rev_cities[0])  # ERROR
# print(len(rev_cities))  # ERROR
for city in rev_cities:
    print(city)
print()


nums = ["123", "841", "851", "444", "237", "988"]
# generator to convert nums elements to ints
# generator to select only nums > 400

r = reversed(cities)
print(r)
r_cities = list(r)
print(r_cities)

city_names = ["Elmira", 'Homestead', 'Durham', 'Albany']
state_names = ['NY', 'PA', 'NC']
places = zip(city_names, state_names)
print(places)
for place in places:
    print(place)
print()

for i, city_name in enumerate(city_names):
    print(i, city_name)
print()

print(enumerate(city_names))
print(list(enumerate(city_names)), '\n')

a = "abc"
b = "def"
print(a + b)

x = [1, 2, 3]
y = [4, 5, 6]
print(x + y)

print('WhooHoo ' * 3)
print(['True'] * 10)
print((5,) * 3)

#  range(start, stop)  range(stop)  range(start, stop, step)
#  range(1, 11), range(10) range(1, 101, 5)
r = range(1, 11)
print(r)
print(r[0])
print(len(r))
for i in r:
    print(i)
print()

for i in range(3):
    print("Hip! Hip! Hooray!!")








