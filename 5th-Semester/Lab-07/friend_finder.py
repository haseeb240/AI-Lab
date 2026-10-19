
from collections import deque


def bfs_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return None

    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            return path

        for friend in graph.get(current, []):
            if friend not in visited:
                visited.add(friend)
                queue.append(path + [friend])

    return None


network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara"],
}

start = "Ali"
goal = "Hira"

path = bfs_shortest_path(network, start, goal)

if path:
    print(f"Shortest chain from {start} to {goal}: {path}")
    print(f"Number of introductions needed: {len(path) - 1}")
else:
    print("No connection found.")
