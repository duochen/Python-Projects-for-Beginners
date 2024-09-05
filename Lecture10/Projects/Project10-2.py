# Maze Solver using Recursion

# The maze is represented as a 2D grid where:
# 0 is a passable path, and 1 is a wall.
# 'S' is the start, 'E' is the end.

maze = [
    ['S', 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 'E']
]

# Directions to move in the maze (down, up, right, left)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(row)
    print()

# Recursive function to solve the maze
def solve_maze(maze, x, y, path):
    # Base case: if we reach the exit
    if maze[x][y] == 'E':
        path.append((x, y))
        return True
    
    # Mark the current cell as visited by setting it to 2
    if maze[x][y] == 0 or maze[x][y] == 'S':
        path.append((x, y))  # Add current position to path
        maze[x][y] = 2  # Mark as visited
        
        # Explore all four directions
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            
            # Check if the new position is within bounds and not visited or a wall
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] in [0, 'E']:
                if solve_maze(maze, new_x, new_y, path):
                    return True
        
        # If none of the directions work, backtrack
        path.pop()
        maze[x][y] = 0  # Unmark the cell (backtrack)
    
    return False

# Find the start position
def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return i, j
    return None

# Driver code
start = find_start(maze)
if start:
    path = []
    if solve_maze(maze, start[0], start[1], path):
        print("Maze solved! Path to exit:")
        print(path)
    else:
        print("No path found.")
else:
    print("No start point found in the maze.")

print("Final maze state:")
print_maze(maze)
