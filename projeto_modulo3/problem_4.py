def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zeros = []
    twos=[]
    ones=[]
    for x in input_list:
        if x == 0:
            zeros.append(x)
        elif x == 2:
            twos.append(x)
        else:
            ones.append(x)
    result =  zeros+ones+twos
    return result


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


#3 test  Cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0])