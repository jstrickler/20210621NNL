#!/usr/bin/python3

for n in range(0, 32):
	#                            0   1
	# print("{:2d} {:10d}".format(n, 2**n))
	print(f"{n:2d} {2 ** n:12d}")
