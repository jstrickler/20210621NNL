import sys   # module with runtime info

print(sys.argv)   # command line, split on non-quoted space

# sys.argc ???

print("sys.argv[0]:", sys.argv[0])  # script name
print("sys.argv[1]:", sys.argv[1])
print(len(sys.argv))
