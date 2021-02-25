def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = float('inf')
    max = float('inf')
    for number in ints:
        if number > max:
            max = number
        elif number < min:
            min = number
    print((min, max))
    return (min, max)

## Example Test Case of Ten Integers

import random

test1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test1)

print ("Pass" if ((0, 9) == get_min_max(test1)) else "Fail")



test2 = [i for i in range(-9, 10)]  # a list containing 0 - 9
random.shuffle(test2)

print ("Pass" if ((-9, 9) == get_min_max(test2)) else "Fail")

test3 = [i for i in range(5, 7)]  # a list containing 0 - 9
random.shuffle(test3)

print ("Pass" if ((5, 6) == get_min_max(test3)) else "Fail")

test4 = []

print ("Pass" if (tuple() == get_min_max(test4)) else "Fail")