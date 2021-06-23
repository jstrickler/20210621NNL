import sys
#  1. get raw Celsius temperature from command line
#      this returns a string -- store in variable
#  2. convert string variable to new float variable using float()
#  3. calculate F temp using formula and variable from #2
#  4. output F temp using print()

raw_celsius = sys.argv[1]  # get value from command line
celsius = float(raw_celsius)  #
fahrenheit = ((9 * celsius) / 5) + 32
# print(fahrenheit)
print(f"{celsius}\u00B0 C is {fahrenheit}\u00B0 F")
