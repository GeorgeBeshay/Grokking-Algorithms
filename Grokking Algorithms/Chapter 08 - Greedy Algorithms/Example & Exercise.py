# --------------------------------------------------- Exercises ---------------------------------------------------
#   -E(8.1):
#       Step 1) Pick the box of the greatest size possible that can fit in the truck
#       Step 2) Pick the next box of the greatest ....
#       No this algorithm won't come up with the optimal solution. However, it will come up with a "good" solution.
#   -E(8.2):
#       Step 1) Pick the item that have the greatest point value assigned to ..
#       Step 2) Repeat .. Pick the second item that have ....
#       No this algorithm won't come up with the optimal solution. However, it will come up with a "good" solution.
#   -E(8.3): NO [Not Sure].
#   -E(8.4): NO
#   -E(8.5): YES
#   -E(8.6): YES
#   -E(8.7): YES
#   -E(8.8): NO [Not Sure].
# ----------------------------------------------------------------------------------------------------------------

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
stations = dict()
stations.update({
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
})
final_stations = set()
while(states_needed):
    states_covered = set()
    best_staion = None
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_staion = station
            states_covered = covered
    final_stations.add(best_staion)
    states_needed -= states_covered
# ---------------------------------------------------------------------------
print(final_stations)