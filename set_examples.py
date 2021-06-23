colors1 = ['red', 'blue', 'green', 'purple', 'yellow']
colors2 = ['green', 'yellow', 'orange', 'red', 'black']

s1 = set(colors1)
s2 = set(colors2)
s2.add('pink')
s1.add('red')
s1.add('red')
s1.add('violet')
print("s1: {}\n".format(s1))
print("s2: {}\n".format(s2))

print("Both (intersection):", s1 & s2)
print("Just one (xor):", s1 ^ s2)
print("All (union):", s1 | s2)
print("Just s1:", s1 - s2)
print("Just s2:", s2 - s1)

foods = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 
         'spam', 'spam', 'spam', 'spam', 'spam', 
         'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']

unique_foods = set(foods)
print("unique_foods: {}\n".format(unique_foods))


