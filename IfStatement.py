# If statements

is_male = True
is_tall = False

# Basic if statement

if is_male:    #if true default
    print("You are a male")
else:
    print("You are NOT a male")

# OR statement - match any of the varables as true
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are NEITHER male or tall")

# AND statement - ALL variables must be true
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You either not tall or not male or both")

# NOT() and elif statements
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):      # If male and NOT tall
    print("you are a short male")
elif not(is_male) and is_tall:      # If NOT male and tall
    print("you are a not a male but are tall")
else:
    print("You either not tall or not male")

# If statements and comparison operators 

def max_num(num1, num2, num3):      # Function, returns largest of the 3 variables passed to it
    if num1 > num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40, 5))

# Comparision operators

# ==           - if both values are equal
# !=           - not equals
# >            - greater than
# <            - less than
# >=           - greater than or equal to
# <=           - less than or equal to

