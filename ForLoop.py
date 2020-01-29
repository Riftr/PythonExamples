# For Loops

for letter in "Bobs Burgers":
    print(letter)                      # Prints out the string, letter by letter

print("---")
friends = ["Jim", "Karen", "Kevin"]    # List - contains 3 values
for friend in friends:				   # Loops over the list	
    print(friend)					   # Prints out each friend in the list

print("---")
for index in range(10):				   # Loops 10 times (0-9)
    print(index)

print("---")
for indexA in range(3, 10):            # Loops 7 times (3-9)
    print(indexA)

print("---")
for indexB in range(len(friends)):     # Another way of doing the first loop using indexes on the string
    print(friends[indexB])

print("---")
for indexC in range(5):				   # Loops 5 times (0-4), contains if statement
    if indexC == 0:
        print("first")
    else:
        print("not first")