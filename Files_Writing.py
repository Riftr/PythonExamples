# Files - Writing to files

f = open("Data/guru99.txt","w+")  # Open file for writing
for i in range(10):               # Write 10 lines to the file
     f.write("This is line %d\r\n" % (i+1))
f.close()

