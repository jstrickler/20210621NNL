alice_count = 0
with open('DATA/alice.txt') as alice_in:
    for i, line in enumerate(alice_in):
        if 'Alice' in line:
            alice_count += 1
print(f"Alice occurred on {alice_count} lines")
print()
with open('DATA/alice.txt') as alice_in:
    alice_contents = alice_in.read()
    alice_count = alice_contents.count('Alice')
    print(f"Alice occurs {alice_count} times")
print()


