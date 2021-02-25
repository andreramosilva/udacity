def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    return binary_search_rec(input_list, number, 0, len(input_list)-1)

def binary_search_rec(arr,number,start,end):

    mid = start + (end-start)//2


    if start >= end:
        return -1
    elif arr[mid] == number:

        return mid
    else:
        left = binary_search_rec(arr, number, start, mid)

        right = binary_search_rec(arr, number, mid+1, end)
        if left > -1:
            return left
        elif right > -1:
            return right
        else:
            return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


#Test CASES
#1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
#2
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#3
test_function([[2, 3, 4, 5, 6, 7, 8, 1], 99])
test_function([[2, 3, 4, 5, 6, 7, 8, 1], 10])
#3
test_function([[], 1])
#test_function([[2, 3, 4, 5, 6, 7, 8, 1], 10])


