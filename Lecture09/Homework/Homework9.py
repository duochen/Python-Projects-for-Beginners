from collections import deque

def print_maze(maze, path=None):
    """
    Prints the maze with the shortest path marked by '*'.
    If a path is provided, it replaces the cells in the path with '*'.

    :param maze: 2D list representing the maze
    :param path: List of tuples representing the path coordinates
    """
    if path:
        # Mark the path on the maze with '*'
        for (x, y) in path:
            maze[x][y] = '*'
    # Print the maze row by row
    for row in maze:
        print(' '.join(str(cell) for cell in row))
    print()  # Add an empty line for better readability

def bfs(maze, start, end):
    """
    Finds the shortest path in a maze using the Breadth-First Search (BFS) algorithm.

    :param maze: 2D list representing the maze (0 for open cell, 1 for wall)
    :param start: Tuple (x, y) representing the starting point
    :param end: Tuple (x, y) representing the ending point
    :return: List of tuples representing the shortest path from start to end
    """
    # Dimensions of the maze
    rows, cols = len(maze), len(maze[0])

    # Queue for BFS (stores the cells to explore next)
    queue = deque([start])

    # Set to keep track of visited cells
    visited = set()
    visited.add(start)

    # Dictionary to store the parent of each cell (used to reconstruct the path)
    parent = {start: None}

    # BFS loop to explore the maze
    while queue:
        # Get the next cell to explore
        current = queue.popleft()

        # If the current cell is the end, we found the shortest path
        if current == end:
            break

        x, y = current  # Current cell coordinates

        # Explore all 4 possible directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy  # Calculate the new cell's coordinates

            # Check if the new cell is within bounds, not a wall, and not visited
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))  # Add the new cell to the queue
                visited.add((nx, ny))  # Mark the new cell as visited
                parent[(nx, ny)] = (x, y)  # Set the parent of the new cell

    # Reconstruct the path from the end to the start using the parent dictionary
    path = []
    while end in parent:
        path.append(end)  # Add the current cell to the path
        end = parent[end]  # Move to the parent of the current cell
        if end is None:
            break  # Stop if we reach the starting point

    # Reverse the path to get it from start to end
    path.reverse()
    return path

def main():
    """
    Main function to set up the maze and find the shortest path.
    """
    # Define the maze (0 for open cells, 1 for walls)
    maze = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    # Starting and ending points
    start = (0, 0)  # Top-left corner
    end = (4, 4)    # Bottom-right corner

    # Find the shortest path using BFS
    path = bfs(maze, start, end)

    # Print the maze with the shortest path
    print("Maze with Path:")
    print_maze(maze, path)

    # Print the shortest path
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
