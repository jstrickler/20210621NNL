# raw_value = input("Enter a number: ")
# value = float(raw_value)

value = 56

if value > 75:
    print("koala")
    print("quokka")
elif value > 50:  # else if
    print("wombat")
    print("wallaby")
else:
    print("kangaroo")
    print("platypus")

print("Done.")

country = 'Burkina Faso'
if "kin" in country:
    print("Yahoooooo")

list1 = ['a', 'b', 'c']
if list1:   # if bool(list1) == True
    print("Molasses")
list2 = []
if list2:
    print("rumble")
else:
    print("tumble")

# True
#  1 5 800002930293023  "Hello" " " True [1] [False]

# False
#  0  ""  []   False None

#  == != > < >= <=

# x == y     x != y    x > y     x < y


debug = True

if debug:
    color = "red"
else:
    color = "green"

print(color)

color = "red" if debug else "green"   # conditional expression

#  color = debug ? "red" : "green"   Java, C++, etc

a = 100
b = 22

if (a < 25) or (b > 18):
    print("marmot")
else:
    print("wildebeest")






