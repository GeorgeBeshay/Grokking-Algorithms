# Note: Dijkstra's Algorithm should not be used on negatively weighted graphs.
# 3 Dictionaries will be used
#   - 1 For Node / Children
#   - 1 For the CURRENT Costs
#   - 1 For the Parent of Each Node
# -------------------------------------------------------------------------------

Graph = {"Start": {"A": 6, "B": 2}}
Graph.update({
    "A": {"Fin": 1},
    "B": {"A": 3, "Fin": 5},
    "Fin": {}
})
# OR
# Graph = dict()
# Graph["Start"] = {}
# Graph["Start"]["A"] = 6
# Graph["Start"]["B"] = 2
# -----------------------------------------------

infinity = float("inf")
CurrentCosts = {
    "A": 6,
    "B": 2,
    "Fin": infinity
}

Parent = {
    "A": "Start",
    "B": "Start",
    "Fin": None
}

# PNL: Processed(Visited) Nodes List.
PNL = []
# ---------------------------------------------------


def Find_Lowest_Cost_Node(CurrentCosts_, PNL_):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in CurrentCosts_:
        cost = CurrentCosts_[node]
        if cost < lowest_cost and node not in PNL_:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def Dijkstra_Algorithm(Graph_, CurrentCosts_, Parent_, PNL_):
    node = Find_Lowest_Cost_Node(CurrentCosts_, PNL_)
    while node is not None:
        cost = CurrentCosts_[node]
        neighbors = Graph_[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if CurrentCosts_[n] > new_cost:
                CurrentCosts_[n] = new_cost
                Parent_[n] = node
        PNL_.append(node)
        node = Find_Lowest_Cost_Node(CurrentCosts_, PNL_)
    return CurrentCosts_


# To Show The Exact Path:
def showPath(Parent, FinishNode, StartNode):
    if Parent[FinishNode] == StartNode:
        print(StartNode, end=" >> ")
        print(FinishNode, end=" >> ")
    else:
        showPath(Parent, Parent[FinishNode], StartNode)
        print(FinishNode, end=" >> ")


# print(Graph)
# print(Graph["Start"])
# print(Graph["Start"]["A"])
# print(Graph["Start"]["B"])
# print(Graph.keys())
# print(Graph["Start"].keys())
# print("---------------------------------------")
# print(CurrentCosts)
# print(Dijkstra_Algorithm(Graph, CurrentCosts, Parent, PNL))
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------

#  E 7.1:
#       A)
#       = Manually: S >> B >> D >> F
#       = Using The Code:
Graph2 = {
    "S": {"A": 2, "B": 5},
    "A": {"B": 8, "D": 7},
    "B": {"C": 4, "D": 2},
    "C": {"F": 3, "D": 6},
    "D": {"F": 1},
    "F": {}
}


CurrentCosts2 = {
    "A": 2,
    "B": 5,
    "C": float("inf"),
    "D": float("inf"),
    "F": float("inf")
}
Parent2 = {
    "A": "S",
    "B": "S",
    "C": None,
    "D": None,
    "F": None
}
PNL2 = []
print("---------------------- SEPARATOR ----------------------")
print("---------------------- E[7.1][A] ----------------------")
print(f"The Weight of The Shortest Path is: {Dijkstra_Algorithm(Graph2, CurrentCosts2, Parent2, PNL2)['F']} ")
print("Path: ", end="")
showPath(Parent2, 'F', 'S')
print("\b\b\b")

#       B)
#       = Manually: S >> A >> B >> F
#       = Using The Code:
Graph3 = {
    "S": {"A": 1},
    "A": {"B": 2},
    "B": {"C": 1, "F": 3},
    "C": {"A": 1},
    "F": {}
}


CurrentCosts3 = {
    "A": 1,
    "B": float("inf"),
    "C": float("inf"),
    "F": float("inf")
}
Parent3 = {
    "A": "S",
    "B": None,
    "C": None,
    "F": None
}
PNL3 = []
print("---------------------- SEPARATOR ----------------------")
print("---------------------- E[7.1][B] ----------------------")
print(f"The Weight of The Shortest Path is: {Dijkstra_Algorithm(Graph3, CurrentCosts3, Parent3, PNL3)['F']} ")
print("Path: ", end="")
showPath(Parent3, 'F', 'S')
print("\b\b\b")

#       C)
#       = Manually: S >> A >> F
#       = Using The Code:
#       = Note: DIJKSTRA'S ALGORITHM SHOULD NOT BE USED, [NEGATIVELY WEIGHTED GRAPHS].
Graph4 = {
    "S": {"A": 2, "B": 2},
    "A": {"F": 2, "C": 2},
    "B": {"A": 2},
    "C": {"B": -1, "F": 2},
    "F": {}
}


CurrentCosts4 = {
    "A": 2,
    "B": 2,
    "C": float("inf"),
    "F": float("inf")
}
Parent4 = {
    "A": "S",
    "B": "S",
    "C": None,
    "F": None
}
PNL4 = []
print("---------------------- SEPARATOR ----------------------")
print("---------------------- E[7.1][C] ----------------------")
print(f"The Weight of The Shortest Path is: {Dijkstra_Algorithm(Graph4, CurrentCosts4, Parent4, PNL4)['F']} ")
print("Path: ", end="")
showPath(Parent4, 'F', 'S')
print("\b\b\b")
