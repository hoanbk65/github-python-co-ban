
def calculate_power(base, exponent):
    result = 1
    for index in range(exponent):
        result *= base
    return result


print(calculate_power(5, 2))