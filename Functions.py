
# Functions
# - lowercase
# - use underscore
# See PEP8 for naming conventions 

def say_hi(name, age):   								# Function called "say_hi", requires 2 variables 
    print("Hello " + name + ", you are " + str(age))    # Note indent, this statement is part of the function 

say_hi("Mike", 35)										# Not indented, part of the main block of code
say_hi("Steve", 70)									    # Calls our function, passes a string and a number

# Return statement
def cube(num):					# New function, called cube, requires 1 variable
    return num*num*num          # Return - returns a value to whatever called it

result = cube(4)				# Usage example, stores the value from return in the variable called result
print(result) 
