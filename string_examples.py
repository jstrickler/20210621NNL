s1 = "spam\n"
print(s1)
s2 = 'spam\n'
print("done.")
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'


print("It's a Python thing")
print('It is a "Python" thing')
print("""It's a "Python" ''  "" thing""")


# C:   'a' is char  "a" is string   "foo\n"   'foo\n'

x = "a"
y = ""
z = " "
p = "h"
m = "Mississippi"

print(ord(x))
print(chr(97))



# \n \r \b \t \f

print("aaa")  # "aaa" + "\n"
print()  # "\n"
print("bbb")
print("\n")  # "\n" + "\n"

actor = "Chris Hemsworth"

a = actor.upper()
print(a, actor)

print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.count('worth'))
print()
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))  # wilLIAM
print()
print(actor.endswith('garbanzo'))

print(actor)
print(actor.find('em'))
print(actor.find('Chris'))
print(actor.find('Liam'))

rec = "blue:123:apple:wombat"
fields = rec.split(':')
print(fields)
rec = "big  \t    turtle    in\n   space"  # A'tuin :-)
fields = rec.split()
print(fields)

x = ','.join(fields)  # join sequence into string
print(x)
print("===".join(fields))
print(''.join(fields))
print()

s = "       All my exes live in Texas        "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = "xyxxxyyyAll my exes live in Texasyxyyyxxx"
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')
print()

# S.method()
print(len(s), type(s))













