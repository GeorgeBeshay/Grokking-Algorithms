def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append(arr.pop(findSmallest(arr)))
    return newArr


print(selectionSort([7, 9, 2, -2, 100, -500, 9999]))
