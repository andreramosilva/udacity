def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Base cases
    if (number == 0 or number == 1):
        return number

        # Staring from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1;
    result = 1
    while (result <= number):
        i += 1
        result = i * i

    return i - 1

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")