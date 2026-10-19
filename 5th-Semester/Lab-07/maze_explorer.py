
def dfs_can_reach(maze, start, exit_room):
    visited = set()
    visit_order = []

    def dfs(room):
        visited.add(room)
        visit_order.append(room)

        if room == exit_room:
            return True

        for next_room in maze.get(room, []):
            if next_room not in visited:
                if dfs(next_room):
                    return True

        return False

    reachable = dfs(start) if start in maze else False

    print("Visit order:", visit_order)
    return reachable


maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": [],
}

result = dfs_can_reach(maze, "Entrance", "Exit")
print(f"Can reach Exit from Entrance? {result}")
