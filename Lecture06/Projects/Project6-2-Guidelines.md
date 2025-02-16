## **Python Project 2: Debugging a Maze Solver**
### **Step-by-Step Guide**

### **Step 1: Understanding the Problem**
Before jumping into debugging, students should understand the project goals:
- The program should use **Depth-First Search (DFS)** to find a path from the start to the end in a given maze.
- The maze is represented as a **2D list**, where:
  - `0` represents an open path.
  - `1` represents a wall (cannot be crossed).
  - `'S'` represents the starting position.
  - `'E'` represents the ending position.
- The DFS algorithm should navigate through the maze and return a valid path if one exists.

### **Step 2: Running the Buggy Code**
Students should **run the provided code** and observe the errors that appear.

1. Copy the buggy code below and save it as `buggy_maze_solver.py`:
   ```python
   def solve_maze(maze, start, end):
       rows, cols = len(maze), len(maze[0])
       visited = [[False] * cols for _ in range(rows)]
       path = []
       
       def dfs(x, y):
           if x == end[0] and y == end[1]: # Found the end point
               path.append((x, y))
               return True
           
           if x < 0 or y < 0 or x >= rows or y >= cols or maze[x][y] == 1 or visited[x][y]:
               return False  # Out of bounds or wall
           
           visited[x][y] = True
           path.append((x, y))
           
           # Explore neighbors (up, down, left, right)
           if dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1):
               return True
           
           path.pop()  # Backtrack
           return False

       if dfs(start[0], start[1]):
           return path
       else:
           return None  # No valid path found

   # Example maze
   maze = [
       [0, 1, 0, 0, 0],
       [0, 1, 0, 1, 0],
       [0, 0, 0, 1, 0],
       [1, 1, 0, 1, 0],
       [0, 0, 'S', 0, 'E']
   ]

   start = (4, 2)
   end = (4, 4)

   solution = solve_maze(maze, start, end)
   print("Path found:", solution)
   ```

2. **Expected errors or issues:**
   - Index errors due to incorrect checks in `dfs()`.
   - Logic errors in handling the start and end positions.
   - Possible infinite recursion or failure to find a path.

### **Step 3: Identifying and Debugging Errors**
Now, students will debug the program using different techniques:

#### **Method 1: Read the Error Messages**
1. Run the program and **note any error messages**.
2. Use **print statements** to track the values of `x`, `y`, and `path` at different points in the DFS function.
   ```python
   print(f"Visiting: ({x}, {y})")
   ```

#### **Method 2: Step Through Code Using `pdb`**
Python’s built-in debugger (`pdb`) allows step-by-step execution.

1. Insert the following line before calling `dfs()`:
   ```python
   import pdb; pdb.set_trace()
   ```
2. Run the script and use commands like:
   - `n` (next line)
   - `p variable_name` (print variable)
   - `c` (continue execution)

#### **Method 3: Logic Analysis**
Check if the algorithm correctly:
- Marks visited nodes.
- Explores all possible paths.
- Backtracks correctly when encountering dead ends.

### **Step 4: Fixing the Bugs**
Students should now **fix** the identified issues.

1. **Fix incorrect boundary checks** in `dfs()`:
   ```python
   if x < 0 or y < 0 or x >= rows or y >= cols:
       return False  # Out of bounds
   if maze[x][y] == 1 or visited[x][y]:
       return False  # Wall or already visited
   ```

2. **Ensure `'S'` and `'E'` are handled correctly**:
   - Convert `'S'` and `'E'` to `0` at the beginning to allow traversal.

3. **Fix recursion return condition**:
   ```python
   if dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1):
       return True  # If any direction leads to the goal
   ```

### **Step 5: Testing the Corrected Code**
1. Run the corrected version of the program and verify the output.
2. Modify the maze to test different cases:
   - No valid path.
   - Multiple paths.
   - Larger mazes.

### **Step 6: Extend the Project**
Once debugging is complete, students can:
1. **Implement Breadth-First Search (BFS)** for comparison.
2. **Visualize the maze-solving process** using `matplotlib` or `pygame`.
3. **Create dynamic mazes** with random obstacles.

---

### **Final Corrected Code**
```python
def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    path = []
    
    def dfs(x, y):
        if (x, y) == end:
            path.append((x, y))
            return True
        
        if x < 0 or y < 0 or x >= rows or y >= cols or maze[x][y] == 1 or visited[x][y]:
            return False  # Out of bounds or wall
        
        visited[x][y] = True
        path.append((x, y))

        if dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1):
            return True
        
        path.pop()  # Backtrack
        return False

    # Convert start and end to normal numbers for traversal
    sx, sy = start
    ex, ey = end
    maze[sx][sy] = 0
    maze[ex][ey] = 0

    if dfs(sx, sy):
        return path
    return None

# Example Maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 'S', 0, 'E']
]

start = (4, 2)
end = (4, 4)

solution = solve_maze(maze, start, end)
print("Path found:", solution)
```

---

### **Project Summary**
- **Objective**: Debug a DFS-based maze solver.
- **Key Learning Points**:
  - Identifying syntax and logic errors.
  - Using debugging tools like `pdb` and `print()`.
  - Understanding depth-first search (DFS).
  - Writing and testing robust Python code.