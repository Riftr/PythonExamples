# Lists

friends = ["Kevin", "Karen", "Jim", "Oscar", "Tom"] # Basic list
print(friends)
print(friends[0])     # First item in list
print(friends[2])
print(friends[-1])    # Last item in list
print(friends[1:])    # Position 1 onwards
print(friends[1:3])   # Position 1 up to BUT NOT INCLUDING 3 (grabs 2 elements)
friends[1] = "Mike"   # Change Karen in list to Mike
print(friends[1])

# List functions
lucky_numbers = [42, 4, 8, 15, 16, 23]
friends_A = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
friends_B = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
friends_C = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
friends_D = ["Kevin", "Karen", "Jim", "Oscar", "Tom", "Jim"]
friends_E = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
friends_F = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
friends_G = ["Kevin", "Karen", "Jim", "Oscar", "Tom", "Kevin"]
friends_H = ["Kevin", "Karen", "Jim", "Oscar", "Tom", "Jim"]
friends_I = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]


friends_A.extend(lucky_numbers) # Extend - take a list and append anoter list to it
print(friends_A)
friends_B.append("Creed")       # Append - add an element to the END of the list
print(friends_B)
friends_C.insert(1, "Kelly")    # Insert - (index, value) - insert an element at index, pushes others up
print(friends_C)
friends_D.remove("Jim")         # Remove - remove the first occurance of element from the list
print(friends_D)
friends_E.clear()               # Clear - remove all elements from list, gives empty list
friends_F.pop()                 # Pop  -  remove an element from the end of the list
print(friends_F)
print(friends_G.index("Kevin")) # Index - returns the index if element is in the list (first instance), else returns error
print(friends_H.count("Jim"))   # Count - counts the number of times an element appars in the list
friends_I.sort()                # Sort - Sorts the list, alphabetical order
print(friends_I)
lucky_numbers.sort()            # Sorts the list in ascending order (low to high)
print(lucky_numbers)
lucky_numbers.reverse()         # Reverse - reverse sort the order of the list (high to low etc)
print(lucky_numbers)
friends2 = friends.copy()       # Copy - copies a list to another list
print(friends2)