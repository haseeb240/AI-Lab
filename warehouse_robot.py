warehouse = {
    "Receiving": {"Aisle1": 40, "Aisle2": 70},
    "Aisle1": {"Aisle2": 30, "Packing Station": 90},
    "Aisle2": {"Packing Station": 35},
    "Packing Station": {},
}
heuristic = {
    "Receiving": 100,
    "Aisle1": 70,
    "Aisle2": 35,
    "Packing Station": 0,
}
def a_star(start, goal):
    frontier = [(heuristic[start], 0, [start])]
    nodes_explored = 0

    while frontier:
        frontier.sort(key=lambda item: item[0])
        f_cost, g_cost, path = frontier.pop(0)

        current = path[-1]
        nodes_explored += 1

        print(
            f"Exploring {current}: "
            f"g={g_cost}, h={heuristic[current]}, f={f_cost}"
        )

        if current == goal:
            print("Path found by A*:", path)
            print("Total cost of this path:", g_cost)
            print("Total nodes explored:", nodes_explored)
            return path, g_cost

        for neighbor, distance in warehouse[current].items():
            if neighbor not in path:
                new_g = g_cost + distance
                new_f = new_g + heuristic[neighbor]
                new_path = path + [neighbor]

                frontier.append((new_f, new_g, new_path))

    print("No path found.")
    print("Total nodes explored:", nodes_explored)
    return None, float("inf")


a_star("Receiving", "Packing Station")
