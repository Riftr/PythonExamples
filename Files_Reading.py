import os   # Only needed for the last example

# Reading files
# Note, no error checking in these examples


# Open file for reading
employee_file = open("Data/employees.txt", "r")


if employee_file.readable():   # Check if we can *read* the file, bool
	print("We can read file")
else:
	print("Could not open file for reading")
	sys.exit()

print("Please choose an option")
print("1. Whole file")
print("2. A line then another line")
print("3. Whole file as a list")

whichprint = int(input("1, 2, 3: "))
if whichprint == 1:
	print(employee_file.read())       # Prints out the whole file
elif whichprint == 2:
	print(employee_file.readline())   # Prints out a line
	print(employee_file.readline())   # Prints out the next line
elif whichprint == 3:
	print(employee_file.readlines())  # Puts all the lines in a list, can access like a list []

employee_file.close() # Close file when done


# Looping over lines in a file
# Open file for reading again, back at the start of the file
print("---")

employee_file_b = open("Data/employees.txt", "r")

for employee in employee_file_b.readlines():  # Loop over the file
    print(employee)

employee_file_b.close() 


# Putting lines into a list variable
print("---")

employee_file_c = open("Data/employees.txt", "r")

employee_list = employee_file_c.readlines()  # Put each line into a list variable
for employee in employee_list:
    print(employee)

employee_file_c.close() 