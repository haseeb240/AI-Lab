graph = {
    "S": {"A": 6, "B": 5, "C": 10},
    "A": {"E": 6},
    "B": {"E": 6, "D": 7},
    "C": {"D": 6},
    "D": {"F": 6},
    "E": {"F": 4},
    "F": {"G": 3},
    "G": {},
}
heuristic = {
    "S": 17,
    "A": 10,
    "B": 13,
    "C": 4,
    "D": 2,
    "E": 4,
    "F": 1,
    "G": 0,
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
            print("Nodes explored:", nodes_explored)
            print("Path found by A*:", path)
            print("Total cost of this path:", g_cost)
            return path, g_cost

        for neighbor, weight in graph[current].items():
            new_g = g_cost + weight
            new_f = new_g + heuristic[neighbor]
            new_path = path + [neighbor]

            frontier.append((new_f, new_g, new_path))

    print("No path found.")
    print("Nodes explored:", nodes_explored)
    return None, float("inf")


a_star("S", "G")
