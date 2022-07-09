
# Implementing The Graph Using A Hash Table.

graph = dict()
graph.update({"You": ["Alice", "Bob", "Claire"]})
# print(graph.items())
#
# print(graph.keys())
# print(graph.values())
#
# print(graph["You"])

graph.update({"Bob": ["Peggy", "Anuj"]})
graph.update({"Alice": ["Peggy"]})
graph.update({"Claire": ["Jonny", "Thom"]})
graph.update({"Peggy": []})
graph.update({"Anuj": []})
graph.update({"Jonny": []})
graph.update({"Thom": []})


def Print_Nodes(graph, Root):
    if len(graph[Root]) > 0:
        print(Root + "'s Node Points To:")
        for item in graph[Root]:
            print("\t" + item)
        print("-----------------------")
        for item in graph[Root]:
            Print_Nodes(graph, item)
        else:
            return
    else:
        print(Root + "'s Node Points To Nothing !!")
        print("-----------------------")
        return


print("\n")

Print_Nodes(graph, "You")
