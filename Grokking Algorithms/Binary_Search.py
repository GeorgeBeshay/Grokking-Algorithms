def binary_search(input_list, item):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = round((low+high)/2)
        if item == input_list[mid]:
            return mid
        if item > input_list[mid]:
            low = mid + 1
        if item < input_list[mid]:
            high = mid - 1
    else:
        return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))     # => 1
print(binary_search(my_list, -9))    # => None

# Exercises
# 1.1 => 7
# 1.2 => 8
