
import heapq


def ucs_cheapest_route(graph, start, goal):
    if start not in graph or goal not in graph:
        return None, float("inf")

    # Priority queue entries: (total cost, route)
    priority_queue = [(0, [start])]
    best_cost = {start: 0}

    while priority_queue:
        cost, route = heapq.heappop(priority_queue)
        city = route[-1]

        # Skip an outdated, more expensive entry.
        if cost > best_cost.get(city, float("inf")):
            continue

        print(f"Exploring route: {route}, Cost: {cost}")

        if city == goal:
            return route, cost

        for next_city, price in graph.get(city, []):
            new_cost = cost + price

            if new_cost < best_cost.get(next_city, float("inf")):
                best_cost[next_city] = new_cost
                heapq.heappush(
                    priority_queue,
                    (new_cost, route + [next_city])
                )

    return None, float("inf")


flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": [],
}

route, total_cost = ucs_cheapest_route(
    flights, "Islamabad", "Quetta"
)

if route is not None:
    print("Cheapest route:", route)
    print("Total ticket cost:", total_cost)
else:
    print("No route found.")
