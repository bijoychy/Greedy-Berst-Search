import heapq

# Heuristic function: Manhattan distance (simple heuristic for grid)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Greedy Best-First Search function
def greedy_best_first_search(grid, start, goal):
    open_list = []  # Priority queue
    heapq.heappush(open_list, (0, start))  # (f, node) where f = heuristic value
    came_from = {}  # For path reconstruction
    g_score = {start: 0}  # g(n) - cost from start to the node
    f_score = {start: heuristic(start, goal)}  # f(n) = g(n) + h(n), h(n) is the heuristic

    visited = set()  # Set to keep track of visited nodes

    while open_list:
        _, current = heapq.heappop(open_list)  # Get node with lowest f(n)

        # If we reached the goal, reconstruct the path
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        visited.add(current)

        # Explore neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check boundaries and obstacles
            if (
                0 <= neighbor[0] < len(grid)
                and 0 <= neighbor[1] < len(grid[0])
                and grid[neighbor[0]][neighbor[1]] == 0
                and neighbor not in visited
            ):
                tentative_g_score = g_score[current] + 1  # Assume uniform cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # Update g and f scores, add neighbor to open list
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
                    came_from[neighbor] = current

    return None  # No path found

# Reconstruct the path from the came_from map
def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    return path[::-1]  # Return reversed path

# Define the grid (0 = open, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)  # Starting position
goal = (4, 4)  # Goal position

# Run Greedy Best-First Search
path = greedy_best_first_search(grid, start, goal)

# Display results
if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found.")
