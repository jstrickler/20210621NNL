i1 = 100
i2 = 0b100
i3 = 0x100
print(i1, i2, i3)
a = 23902392038209832
b = 203984230948203498203948203948209348209348209348209384029384029834
print(a * b)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.23e35

c = 42j
print(c, c.real, c.imag)
c2 = complex(45, 8)
print(c2, '\n')
a = 19
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a // -b)
print(a ** b) # exponent
print(a % b)  # modulus (remainder)
print(a // b, a % b)
print(divmod(a, b))

x = 5
x *= 10  # x = x * 10
x += 25  # x = x + 25
x /= 3   # x = x / 3
print(x)
print()


#  a @ b   matrix mult
#  a * b   itemwise mult

# NO!
#  x++ ++x  x-- --x

a = "100"
b = 25
print(a + str(b))
print(int(a) + b)
print(float(a) + b)

# str() bool()
# int() float() complex()

d = "DeadBeef"
print(int(d, 16))






