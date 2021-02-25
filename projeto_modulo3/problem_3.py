def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #quicksort inplace
    quicksort(input_list)
    num_1_str = ''
    num_2_str = ''
    max_index = 0
    max_sum = 0
    if len(input_list)<=1:
        return input_list
    for i in range(len(input_list)):
        max_num  = input_list.pop()
        if i%2==0:
            num_1_str+=str(max_num)
        else:
            num_2_str+=str(max_num)

    return [int(num_1_str),int(num_2_str)]


#sorting:
def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    sort_all(items, 0, len(items) - 1)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


#test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case2 = [[4, 0, 1, 5, 9, 8], [951, 840]]
test_case3 = [[4, 6, 2, 7, 0, 8], [862, 740]]
test_case4 = [[], []]
test_case5 = [[1, 2], [1, 2]]
test_case6 = [[0, 0], [0, 0]]
test_function(test_case1)
test_function(test_case2)
test_function(test_case3)
test_function(test_case4)
test_function(test_case5)
test_function(test_case6)