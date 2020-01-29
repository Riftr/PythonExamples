from math import *

# Working with Numbers

# Basic maths
print(-2.0987)
print(3 + 4 + 5)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3) # 10 mod 3, spits out remainder

my_num = 7
print(my_num)
print(str(my_num) + " my fav number") # Convert interger to string

# Common number functions, math module not required
my_num = -5
print(abs(my_num))   # Absolute value - basically remove the negative sign if one exists
print(pow(4, 2))     # Powers - number, power (4 raised to the power of 2)
print(max(4, 2))     # Max - returns the larger of the two
print(min(4, 2))     # Min - returns the smaller of the two
print(round(3.2))    # Round - rounds number up or down

# Functions imported from the maths module
print(floor(3.7))    # Floor - grabs the lowest number (rounds down)
print(ceil(3.7))     # Ceil - grabs the highest number (rounds up)
print(sqrt(36))      # Square root - returns sq of a number
