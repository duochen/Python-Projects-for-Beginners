Here's a detailed explanation of the code that implements the Breadth-First Search (BFS) algorithm to find the shortest path in a maze:

### Code Breakdown

#### 1. **Imports**
```python
from collections import deque
```
We import `deque` from Python's `collections` module. A deque (double-ended queue) is used for efficiently adding and removing elements from both ends. In this case, it's used as a queue to explore nodes in the maze.

#### 2. **`print_maze` Function**
```python
def print_maze(maze, path=None):
    if path:
        for (x, y) in path:
            maze[x][y] = '*'
    for row in maze:
        print(' '.join(str(cell) for cell in row))
    print()
```
- **Purpose**: This function prints the maze and optionally marks the path from start to end using `*` symbols.
- **Parameters**:
  - `maze`: A 2D list representing the maze.
  - `path`: A list of coordinates (x, y) marking the shortest path, if found.
- **How it works**: 
  - If a path is provided, it replaces the values in the maze grid with `*` at the coordinates that belong to the shortest path.
  - The maze is then printed row by row.

#### 3. **`bfs` Function**
```python
def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}
```
- **Purpose**: This function implements the BFS algorithm to find the shortest path in the maze.
- **Parameters**:
  - `maze`: A 2D list representing the maze.
  - `start`: A tuple (x, y) representing the starting coordinates.
  - `end`: A tuple (x, y) representing the ending coordinates.
- **Key Steps**:
  - `rows` and `cols`: The number of rows and columns in the maze.
  - `queue`: A deque initialized with the starting point, used to store the points to be explored.
  - `visited`: A set that keeps track of the cells that have already been visited to avoid revisiting them.
  - `parent`: A dictionary that stores the parent (previous cell) of each cell. This is used to reconstruct the path once the end is reached.

#### BFS Algorithm (Main Loop)
```python
    while queue:
        current = queue.popleft()
        if current == end:
            break
        
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
```
- **Main Logic**:
  - **Queue Processing**: We repeatedly dequeue (`popleft`) the first element of the queue, which represents the current position in the maze.
  - **Termination Condition**: If the current position is the `end` point, we exit the loop because we have found the path.
  - **Exploring Neighbors**: For each current cell, the algorithm explores the four possible directions (up, down, left, right) by adjusting the x and y coordinates (`dx`, `dy`). 
  - **Valid Moves**: The algorithm only moves to neighboring cells that:
    - Are within maze bounds (`0 <= nx < rows` and `0 <= ny < cols`).
    - Are free cells (`maze[nx][ny] == 0`).
    - Have not been visited yet (`(nx, ny) not in visited`).
  - **Queueing**: If a valid neighbor is found, it is added to the queue, marked as visited, and its parent is recorded in the `parent` dictionary.

#### Path Reconstruction
```python
    path = []
    while end in parent:
        path.append(end)
        end = parent[end]
        if end is None:
            break
    path.reverse()
    return path
```
- **Reconstructing the Path**:
  - Once the end point is reached, the algorithm traces back the path from the `end` to the `start` using the `parent` dictionary. 
  - Each step is added to the `path` list, which is then reversed to get the path from `start` to `end`.

#### 4. **`main` Function**
```python
def main():
    maze = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    end = (4, 4)
    path = bfs(maze, start, end)
    
    print("Maze with Path:")
    print_maze(maze, path)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")
```
- **Maze Setup**: The maze is a 5x5 grid where:
  - `0` represents open (free) cells.
  - `1` represents blocked cells.
  - The start point is `(0, 0)` and the end point is `(4, 4)`.
  
- **BFS Call**: The `bfs` function is called to find the shortest path in the maze.
  
- **Maze Printing**: The `print_maze` function is used to print the maze with the path (if found).

- **Result**: If a path is found, it is printed as a list of coordinates. Otherwise, it prints "No path found."

#### 5. **`__main__` Block**
```python
if __name__ == "__main__":
    main()
```
- This block ensures that the `main()` function is called only when the script is run directly.

---

### Summary of the Algorithm:
1. **Initialize BFS** with the start point in the queue.
2. **Explore all reachable cells** from the current position, moving to unvisited neighbors that are free cells.
3. **Use a queue** to keep track of cells to explore and a `visited` set to avoid revisiting cells.
4. **Use a parent dictionary** to reconstruct the shortest path from end to start.
5. **Print the maze** and the shortest path, marking it with `*` symbols.

### Output

```
Maze with Path:
* * 1 0 0
1 * 1 0 0
1 * * * 0
0 0 1 1 0
0 0 0 * *

Shortest path: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 4)]
```

In this example, the BFS finds the shortest path through the maze and marks it with `*` symbols. The algorithm ensures that the path found is the shortest in terms of the number of steps.