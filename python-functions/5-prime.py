def is_prime(number):
    if number < 2:
        return False
    for j in range(2, number):
        if number % j == 0:
            return False
    return True