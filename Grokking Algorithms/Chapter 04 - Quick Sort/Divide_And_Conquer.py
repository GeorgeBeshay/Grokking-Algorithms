# Divide And Conquer Concept
# Figure out the best / base case
# Figure out how to divide your problem in order to reach the best case


# -----------------------------------------------------------
# ----------------------- Functions Definition --------------
# -----------------------------------------------------------
# Array Elements Total Without Recursion
def Sum(arr):
    total = 0
    for i in arr:
        total += i
    return total


# Array Elements Total Using Recursion
def Sum_Pro(arr):
    return Sum_Recursive(arr, 0, len(arr)-1)


def Sum_Recursive(arr, i, j):
    if i == j:
        return arr[i]
    elif i > j:
        return 0
    else:
        return arr[i] + Sum_Recursive(arr, i+1, j)


def Max_Num_In_A_List(arr):
    if len(arr) != 0:
        return Max_Recursive(arr, arr[0], 1, len(arr) - 1)
    else:
        return None


def Max_Recursive(arr, max, start, end):
    if arr[start] > max:
        max = arr[start]
    if start < end:
        return Max_Recursive(arr, max, start + 1, end)
    else:
        return max


# -----------------------------------------------------------
# ----------------------- Driver Code -----------------------
# -----------------------------------------------------------
S1 = Sum([5, 2, 4, 1, 5, 101, 4324, 23, 42, -78])
S2 = Sum_Pro([5, 2, 4, 1, 5, 101, 4324, 23, 42, -78])

if S1 == S2:
    print(f"S1 & S2 Are Equal To {S1} !!")
else:
    print(f"S1 & S2 Are Not Equal !!\nS1 = {S1}\nS2 = {S2}")

print(Max_Num_In_A_List([5, 2, 4, 1, 5, 101, 4324, 23, 42, -78]))
print(Max_Num_In_A_List([]))
