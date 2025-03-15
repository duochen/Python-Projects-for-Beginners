### **Step-by-Step Guidelines for Maze Solver Using Recursion**

---

## **Step 1: Understanding the Problem**
Before coding, students should understand how a maze solver works using recursion and backtracking.

### **How It Works**
- A maze is a 2D grid with **walls (`#`)** and **paths (`.`)**.
- The solver starts at an entrance (`S`) and must find a path to the exit (`E`).
- The program will **try different paths recursively** until it finds a valid route.

---

## **Step 2: Define the Maze Representation**
The maze can be represented as a **2D list (grid)** in Python.

### **Example Maze Representation**
```python
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '#', 'E', '#'],
    ['#', '#', '#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
```
- `'S'`: Start position
- `'E'`: Exit position
- `'.'`: Open path
- `'#'`: Wall (cannot pass)

---

## **Step 3: Define Helper Functions**
### **3.1. Locate Start and End Points**
Students should write a function to **find the coordinates of `S` and `E`**.

```python
def find_positions(maze, symbol):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == symbol:
                return (row, col)  # Return the coordinates of the symbol
    return None  # Return None if symbol not found
```

---

## **Step 4: Implement the Recursive Solver**
### **4.1. Recursive Function to Explore Paths**
The recursive function should:
- Check if the current position is the exit.
- Mark the current path as **visited** (`'*'`).
- Move in all possible directions (up, down, left, right).
- If a dead-end is reached, backtrack (undo marking).

```python
def solve_maze(maze, row, col):
    # Base Case: If we reach the exit
    if maze[row][col] == 'E':
        return True

    # Check if we are on a valid path
    if maze[row][col] != '.' and maze[row][col] != 'S':
        return False

    # Mark the current position as visited
    maze[row][col] = '*'

    # Explore all four directions: down, right, up, left
    if (solve_maze(maze, row + 1, col) or  # Down
        solve_maze(maze, row, col + 1) or  # Right
        solve_maze(maze, row - 1, col) or  # Up
        solve_maze(maze, row, col - 1)):   # Left
        return True

    # Backtrack (undo marking)
    maze[row][col] = '.'
    return False
```

---

## **Step 5: Run the Solver**
### **5.1. Combine Everything and Run the Solver**
Students should:
1. **Find** the start position.
2. **Call the recursive function**.
3. **Print** the final maze showing the solution.

```python
def print_maze(maze):
    for row in maze:
        print(" ".join(row))
    print()

# Main function to run the maze solver
def main():
    maze = [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', '.', '.', '#', 'E', '#'],
        ['#', '#', '#', '.', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#']
    ]

    start_pos = find_positions(maze, 'S')

    if start_pos:
        if solve_maze(maze, start_pos[0], start_pos[1]):
            print("Maze solved:")
        else:
            print("No solution found.")
        print_maze(maze)
    else:
        print("Start position not found.")

if __name__ == "__main__":
    main()
```

---

## **Step 6: Test Different Mazes**
Students can modify the **maze structure** to test different scenarios:
- A maze with no solution.
- A more complex maze.
- A larger maze.

---