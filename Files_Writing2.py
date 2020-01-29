# Writing files 2

# Append a line to a file
employee_file = open("Data/employees_add.txt", "a")
employee_file.write("\n" + "Toby - Human Resources") # \n add new line then text
employee_file.close()

# W - overwrite the whole file (all contents will be lost), will create a file if not found
employee_file2 = open("Data/employees_overwrite.txt", "w")
employee_file2.write("Some text") # \n add new line then text
employee_file2.close()

'''
Modes when opening a file:

  r  – Read only
  w  – Write mode, will overwrite file completely
  a  – Appending mode, add data to the end
  r+ – Special read and write mode
  X  - Create file, error if exists
  
  Additions (e.g. Xt):
  t - text
  b - binary
'''

# With and Open statements. Closes file for us automatically when complete

# Open file for writing (note: still overwrites file)
with open("Data/employees_object.txt", "w") as file:
    file.write("Jim - Salesman\n")
    file.write("Caitlyn - CEO")

# Opening file for reading
with open("Data/employees.txt", "r") as another_file:
	more_data = another_file.readlines()
	for line in more_data:
		print(line)

# Reading all the lines into a list and iterating over them
with open("Data/employees_object.txt") as f:
    data = f.readlines()
    for line in data:
        print(line)
