from collections import deque

# BFS implementation
def bfs(graph, start, goal):
    queue = deque([(start, [start])])  # Queue stores (current node, path)

    while queue:
        current, path = queue.popleft()

        # Check if the current node is the goal
        if current == goal:
            return path  # Return the path to the goal

        # Explore neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return None  # If no path is found

# Example graph for BFS
graph_bfs = {
    1: [7, 8, 3],
    7: [4, 20, 17],
    8: [6],
    3: [9, 12],
    9: [19],
    4: [42],
    20: [28],
    17: [10]
}

# Run BFS
start_bfs = 1
goal_bfs = 19
path_bfs = bfs(graph_bfs, start_bfs, goal_bfs)
print("BFS Path:", path_bfs)


# DFS implementation
def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]

    # Check if the current node is the goal
    if start == goal:
        return path  # Return the path to the goal

    # Explore neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path + [neighbor])
            if new_path:
                return new_path

    return None  # If no path is found

# Example graph for DFS
graph_dfs = {
    1: [7, 8, 3],
    7: [4, 20, 17],
    8: [6],
    3: [9, 12],
    9: [19],
    4: [42],
    20: [28],
    17: [10]
}

# Run DFS
start_dfs = 1
goal_dfs = 19
path_dfs = dfs(graph_dfs, start_dfs, goal_dfs)
print("DFS Path:", path_dfs)
