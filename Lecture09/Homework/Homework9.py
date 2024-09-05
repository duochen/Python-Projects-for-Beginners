from collections import deque

def print_maze(maze, path=None):
    if path:
        for (x, y) in path:
            maze[x][y] = '*'
    for row in maze:
        print(' '.join(str(cell) for cell in row))
    print()

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

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

    path = []
    while end in parent:
        path.append(end)
        end = parent[end]
        if end is None:
            break
    path.reverse()
    return path

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

if __name__ == "__main__":
    main()
