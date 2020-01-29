#2 Dimensional lits
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])  # Accessing 0,0 (prints 1)
print(number_grid[2][1])  # Accessing 2,1 (prints 8)

print("---")
for row in number_grid:   # Accessing each row
    print(row)

print("---")
for row in number_grid:
    for column in row:
        print(column)     # Accessing each individual element in each row using nested loops
