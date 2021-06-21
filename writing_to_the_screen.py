a = "Joe Dough"
b = 4783
c = 123.3902390932

print()
print(a)
print(a, b, c)
# sep = ' '
# end = '\n'
# print(str(a) + sep + str(b) + sep + str(c) + end

print(a, b, c, sep="/")
print(a, b, c, sep=", ")
print(a, b, c, sep="")
print(a, b, c, sep=" ")
print()

print(a, end=' ')
print(b, end= ' + ')
print(c)
print()

#   printf("%.1f", c);
print("{:.1f}".format(c))

print("{} owes ${}".format(a, b))
# 3.6 and later
print(f"{a} owes ${b}")  # f-string

print("%s owes $%d" % (a, b)) # legacy formatting


