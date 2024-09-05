def solve_maze(maze, start, end, path=[]):
    """Finds a path from start to end in the maze using DFS."""
    x, y = start
    
    # Check if we reached the end
    if (x, y) == end:
        return path + [end]

    # Mark the current cell as visited (assume 1 is wall, 0 is path, 2 is visited)
    maze[x][y] = 2
    
    # Explore neighbors (up, down, left, right)
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    for nx, ny in neighbors:
        # Check if the next move is valid
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            new_path = solve_maze(maze, (nx, ny), end, path + [(x, y)])
            if new_path:
                return new_path
    
    # Unmark the current cell for backtracking
    maze[x][y] = 0
    
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
