campus = {
    "Hostel": {"Cafeteria": 150, "Admin Block": 300},
    "Cafeteria": {"Academic Block": 200},
    "Admin Block": {"Academic Block": 120},
    "Academic Block": {"Library": 100},
    "Library": {},
}
heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Academic Block": 90,
    "Library": 0,
}
def gbfs(start, goal):
    frontier = [(heuristic[start], 0, [start])]
    nodes_explored = 0
    while frontier:
        frontier.sort(key=lambda item: item[0])
        h_cost, path_cost, path = frontier.pop(0)
        current = path[-1]
        nodes_explored += 1
        print(f"Exploring {current}, h={h_cost}")
        if current == goal:
            print("Path found by GBFS:", path)
            print("Total cost of this path:", path_cost)
            print("Nodes explored:", nodes_explored)
            return path, path_cost

        for neighbor, distance in campus[current].items():
            if neighbor not in path:
                new_cost = path_cost + distance
                frontier.append(
                    (heuristic[neighbor], new_cost, path + [neighbor])
                )

    print("No path found.")
    return None, float("inf")
gbfs("Hostel", "Library")
