
#  1. ask user for Celsius temperature using input()
#      this returns a string -- store in variable
#      raw_temp = input("Enter temp in C: ")
#  2. convert string variable to new float variable using float()
#  3. calculate F temp using formula and variable from #2
#  4. output F temp using print()

raw_celsius = input("Enter temperature in C: ")
celsius = float(raw_celsius)
fahrenheit = ((9 * celsius) / 5) + 32
# print(fahrenheit)
print(f"{celsius}\u00B0 C is {fahrenheit}\u00B0 F")
