# Working with Strings

# Variable = value
character_name = "Bob"  # Basic string - being stored in a variable called character_name
character_age = 36      # Number - stored in a variable (not a string!)
is_male = True          # Boolean - can only be True or False

# Concatinating some strings and variables together and printing them
# Note str(variable) converts the Interger value to a string
print("Once there was a man named " + character_name + ". They were " + str(character_age) + " years old.")

character_name = "John" # Change the character_name variable to a different value (John)
print("Once there was a man named " + character_name + ". They were " + str(character_age) + " years old.")


print("Length is " + str(len(character_name)))  # Prints out: John    | Note the use of str() and len()
print("To upper: " + character_name.upper())    # Prints out: JOHN     
print(character_name[0]) 						# Prints out: J
print(character_name.index("h"))				# Prints out the position of the first h ie. 2. Can use full words not just one letter. Error if none.
print(character_name.replace("J", "E"))			# Prints out: EOHN    | Replace J with E in the string