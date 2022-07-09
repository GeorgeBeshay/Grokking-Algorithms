from collections import deque

Search_Queue = deque()
Graph = dict()
Root = "You"
Graph.update({"You": ["Alice", "Bob", "Claire"]})
Graph.update({"Bob": ["Peggy", "Anuj"]})
Graph.update({"Alice": ["Peggy"]})
Graph.update({"Claire": ["Jonny", "Thom"]})
Graph.update({"Peggy": []})
Graph.update({"Anuj": []})
Graph.update({"Jonny": []})
Graph.update({"Thom": []})

Search_Queue += Graph[Root]


def Person_Is_Seller(person):
    return person[-1] == 'm'


Visited = Graph[Root]

while Search_Queue:
    print(Search_Queue)
    person = Search_Queue.popleft()
    if Person_Is_Seller(person):
        print(f"{person} is Mango's Seller, The Closest One To You.")
        break
    else:
        if len(Graph[person]) > 0:
            for item in Graph[person]:
                if item in Visited:
                    continue
                else:
                    Search_Queue += [item]
                    Visited.append(item)


# ------------------------------------- Exercises -------------------------------------
# >> E 6.1
#   Up Then Right
# >> E 6.2
#   Up Then Right
# >> E 6.3
#   - A => Invalid
#   - B => Valid
#   - C => Invalid
# >> E 6.4
#   Wake up Should Always Come as the first task in the list.
#   Shower Should Always Come After Exercise (Not Exactly After, But Exercise Should Be Already Done)
#   Get Dressed      "      "      "   "     Shower
#   Eat Breakfast    "      "      "   "    Brush Teeth
# >> E 6.5
#   - A =>  Check
#   - B =>  X
#   - C =>  Check
