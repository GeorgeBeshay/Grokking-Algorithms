# Item_Weight = {
#     "Guitar": 1,
#     "Laptop": 3,
#     "Stereo": 4,
#     "Iphone": 1,
#     "MP3 Player": 1
# }
#
# Item_Price = {
#     "Guitar": 1500,
#     "Laptop": 2000,
#     "Stereo": 3000,
#     "Iphone": 2000,
#     "MP3 Player": 1000
# }
#
# Id = {
#     1: "Guitar",
#     2: "Stereo",
#     3: "Laptop",
#     4: "Iphone",
#     5: "MP3 Player"
# }
#
# Knapsack_Weight = 4
#
# Table = []
#
# for i in range(len(Id)):
#     Table.append([])
#     for j in range(Knapsack_Weight):
#         Table[i].append(0)
#
# for i in range(len(Id)):
#     for j in range(Knapsack_Weight):
#         if i != 0:
#             N = Table[i-1][j]
#         else:
#             N = 0
#         M = 0
#         if j+1 >= Item_Weight[Id[i+1]]:
#             M = Item_Price[Id[i+1]]
#         if i >= 1 and j >= Item_Weight[Id[i+1]]:
#             M += Table[i-1][j-Item_Weight[Id[i+1]]]
#         if N > M:
#             Table[i][j] = N
#         else:
#             Table[i][j] = M
#
#
# for i in range(len(Id)):
#     print(f"{Id[i+1]}: ${Item_Price[Id[i+1]]}: {Item_Weight[Id[i+1]]}lb")
# print("-" * 50)
# print("\t\t", end="")
# for i in range(Knapsack_Weight):
#     print(i+1, end="\t\t")
# print()
# for i in range(len(Id)):
#     print(Id[i+1], end=": ")
#     print(Table[i])

# ------------------------ SEPARATOR ------------------------
# E (9.2):
#   Answer: The Optimal Set Of items to take on your camping trip is:
#       { Water, Jacket, Camera } { Value = 25 }
#   By Using The Code:
#       The Total Value is = 25 which corresponds to the same items mentioned above.

Item_Weight = {
    "Water": 3,
    "Book": 1,
    "Food": 2,
    "Jacket": 2,
    "Camera": 1
}

Item_Price = {
    "Water": 10,
    "Book": 3,
    "Food": 9,
    "Jacket": 5,
    "Camera": 6
}

Id = {
    1: "Water",
    2: "Book",
    3: "Food",
    4: "Jacket",
    5: "Camera"
}

Knapsack_Weight = 6

Table = []

for i in range(len(Id)):
    Table.append([])
    for j in range(Knapsack_Weight):
        Table[i].append(0)

for i in range(len(Id)):
    for j in range(Knapsack_Weight):
        if i != 0:
            N = Table[i-1][j]
        else:
            N = 0
        M = 0
        if j+1 >= Item_Weight[Id[i+1]]:
            M = Item_Price[Id[i+1]]
        if i >= 1 and j >= Item_Weight[Id[i+1]]:
            M += Table[i-1][j-Item_Weight[Id[i+1]]]
        if N > M:
            Table[i][j] = N
        else:
            Table[i][j] = M


for i in range(len(Id)):
    print(f"{Id[i+1]}: ${Item_Price[Id[i+1]]}: {Item_Weight[Id[i+1]]}lb")
print("-" * 50)
print("\t\t", end="")
for i in range(Knapsack_Weight):
    print(i+1, end="\t\t")
print()
for i in range(len(Id)):
    print(Id[i+1], end=":\t")
    # print(Table[i])
    for j in range(len(Table[i])):
        print(Table[i][j], end=",\t\t")
    print("\b\b\b")

# E (9.3):
#               ----------------------------------
#                   |   C   L   U   E   S   |
#               ----------------------------------
#               B   |   0   0   0   0   0   |
#               L   |   0   1   1   1   1   |
#               U   |   0   1   2   2   2   |
#               E   |   0   1   2   3   3   |
#              -----|-----------------------|-----

