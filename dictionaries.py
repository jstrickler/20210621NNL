d1 = dict()  # empty dictionary
d2 = {'TX': 'Texas', 'NC': 'North Carolina', 'NY': 'New York'}
d3 = {}  # empty dict

d3['NC'] = "Raleigh"
d3['NY'] = "Albany"
d3['PA'] = "Harrisburg"

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

print(airports['YOW'])
print(airports['RDU'])
print(airports.get('PIT'))
print(airports.get('OAK'))
print(airports.get('PIT', 'NOT FOUND'))
print(airports, '\n')

print(airports.setdefault('ELM', 'Elmira'))
print(airports, '\n')

airports['ALB'] = 'Albany'
airports['LAX'] = 'Los Angeles'
print(airports, '\n')

for k in 'RDU', 'XYX', 'SFO', 'YOW', 'MUX':
    print(k, k in airports)
print()

for abbr, name in airports.items():  # list of tuples
    print(abbr.lower(), name.upper())
print()

print(airports.keys(), '\n')
print(airports.values(), '\n')

for abbr, name in sorted(airports.items()):  # list of tuples
    print(abbr.lower(), name.upper())
print()










