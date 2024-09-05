# Initial (buggy) implementation of the maze solver

def solve_maze(maze, start, end, path=[]):
    """Finds a path from start to end in the maze using DFS."""
    x, y = start
    
    # Check if we reached the end
    if (x, y) == end:
        return path + [end]

    # Mark the current cell as visited (assume 1 is wall, 0 is path)
    maze[x][y] = 2
    
    # Explore neighbors (up, down, left, right)
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    for nx, ny in neighbors:
        # Check if the next move is valid
        if nx >= len(maze) or ny >= len(maze[0]) or maze[nx][ny] != 0:
            continue  # Skip invalid or blocked paths

        # Recursive call with a bug: missing return value assignment
        solve_maze(maze, (nx, ny), end, path + [(x, y)])

    return None  # No path found

# Example maze (0 = path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

# Start and end points
start = (0, 0)
end = (4, 4)

# Call the solve_maze function and print the result
path = solve_maze(maze, start, end)

if path:
    print("Path found:", path)
else:
    print("No path found!")
