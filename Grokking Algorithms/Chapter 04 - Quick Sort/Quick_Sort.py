import math


def Quick_Sort(arr):
    if len(arr) >= 2:
        Pivot = arr[math.floor(len(arr)/2)]
        SubArray1 = []
        SubArray2 = []
        for i in range(0, len(arr)):
            if i == math.floor(len(arr)/2):
                continue
            if arr[i] <= Pivot:
                SubArray1.append(arr[i])
            else:
                SubArray2.append(arr[i])
        return Quick_Sort(SubArray1) + [Pivot] + Quick_Sort(SubArray2)
    else:  # Base Case 1
        return arr


print(Quick_Sort([33, 10, 15, 7]))
print(Quick_Sort([17, 15]))
print(Quick_Sort([9]))
print(Quick_Sort([]))
print(Quick_Sort([10, 5, 2, 3]))
