# Files - Full example

'''
 When you want to open a file that you will eventually write to, it's usually best to just read the 
 whole file in and store it as an object in memory. Then when you need to save, open the
 file for writing again and rewrite the contents to it.

'''

# Read the file, store in variable
try:
	with open("Data/employees_full.txt") as f:    # Open file, closes file automatically
		employee_file = f.readlines()             # Reads into a list
except IOError as err:
	print("Could not open file, error: " + err)
else:
	print("Opened file successfully")

# Do some stuff, such as add an employee
employee_file.append("\nRobert - Programmer")     # \n is an escape character, means new line

print(employee_file[2])                           # Access an item in the list
print(employee_file[5])                           # Access our new item

# Time to save file
try:
	with open("Data/employees_full.txt", "w") as file:
		for item in employee_file:                # We have to loop over the list, adding line by line
			file.write(item)
except IOError as err:
	print("Could not write file, error: " + err)







