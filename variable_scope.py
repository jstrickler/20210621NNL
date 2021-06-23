
# local, nonlocal, global, builtin

# local global

value = 100  # global variable (global to file/module)

def spam():
    x = "hello"   # local variable (local to function)
    print("value: {}\n".format(value))  # print global var
    
    print("x: {}\n".format(x))  # print local var

spam()
print("value: {}\n".format(value))

# print("x: {}\n".format(x))  INVALID -- x is not defined here




