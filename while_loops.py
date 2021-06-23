i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    animal = input("What is your favorite animal (q to quit)? ")
    if animal == 'q':
        print("Bye")
        break  # exit loop RIGHT NOW (don't do lines 12-13)
    if animal == '':
        continue # go to top of loop
    print(f"I like {animal}s too")  # f-string AKA formatted string
    print()

# for i in range(10):
#     print("something....")