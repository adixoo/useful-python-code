from math import sqrt

def get_factors(number):
    """
    Returns a list of all factors of the given number.
    
    Parameters:
        number (int): The number to find factors for.
    
    Returns:
        list: A list containing all factors of the number.
    """
    factors = []
    square_root = round(sqrt(number))
    for i in range(1, square_root + 1):
        if number % i == 0:
            factors.append(int(number / i))
            factors.append(i)

    return sorted(factors)
