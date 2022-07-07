# Hash Tables are implemented in python, Called Dictionary

Maggie = {
    #  Key: Value
    "Apple": 0.67,
    "Milk": 1.49,
    "Avocado": 1.49
}

Maggie["Egg"] = 6.6

# Note That you can assign the key as a number and the value as the string
# So it is not a must to Be in the form of (String Maps To Number)
# It can be (Number Maps to String)

Phone_Book = {
    # Key: Value
    911: "Emergency"
}


print(Maggie.items())
print(Maggie.keys())
print(Maggie.values())
print(Maggie["Avocado"])

print(Phone_Book.items())


def Did_He_Vote_Before(Name, Dictionary):
    if Dictionary.get(Name) == None:
        print(f"{Name} Didn't Vote Before")
        Dictionary.update({Name: True})
        print(f"Voter {Name} Has Been Added to the Voters List Successfully")
    else:
        print(f"{Name} Voted Before .. Kick Him out !!")


voted = dict({"George": True})
voted.update({"Tom": True})
print(voted)
Did_He_Vote_Before("Youssef", voted)
print(voted)
Did_He_Vote_Before("George", voted)
