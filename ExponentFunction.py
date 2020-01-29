# Exponent functions

print(2**3)  # 2 to the power of 3 or 2^3
print("---")

# Creating our own fuction to do the above manually, as an example
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))


