# Try / Except / Finally example


# Basic handling
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:    # Catches ZeroDivisionError
    print("Divided by 0")
except ValueError as err:    # Cataches ValueError, passes error message
    print("Invalid Input")
    print(err)
except:						 # Catches all errors (not advisable)
	print("Shouldn't do this")
finally:
	print("Always do this")  # Always executes this, regardless of error or not


# Else statement

try:
	print("Some text")
except:
	print("Caught some error")
else:
	print("Didn't catch error") # Executed if no errors occured


# Raise our own errors (Exception)
test_a = 0
if test_a > 10:
	raise Exception("Test was not greater than 10")

# Raise error, define what type
test_b = "some text"
if not type(test_b) is int:
	raise TypeError("Must be an integer")