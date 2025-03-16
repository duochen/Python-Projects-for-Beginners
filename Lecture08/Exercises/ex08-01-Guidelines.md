Here's a clear, step-by-step guide to complete a Python project building a **text-based Tic-Tac-Toe game** that reads moves from a file and updates the game board:

---

### Step-by-Step Project Guide:

### **Step 1: Create the Tic-Tac-Toe Board**

- **Goal:** Create and display an empty 3x3 board using nested lists.

- **Instructions:**  
  ```python
  def create_board():
      return [[' ' for _ in range(3)] for _ in range(3)]

  def display_board(board):
      print("Current Board:")
      for row in board:
          print('|'.join(row))
          print('-' * 5)
  ```

### **Step 2: Read Moves from a File**

- **Goal:** Read moves from a file (`moves.txt`) line by line.

- **Instructions:**
  - Create a file named `moves.txt` with moves formatted like this:
    ```
    X, 0, 0
    O, 1, 1
    X, 0, 1
    O, 1, 0
    X, 0, 2
    ```
  - Use Python file operations to read this file:
  ```python
  def read_moves(filename):
      moves = []
      with open(filename, 'r') as file:
          for line in file:
              player, row, col = line.strip().split(',')
              moves.append((player.strip(), int(row), int(col)))
      return moves
  ```

### **Step 3: Make Moves on the Board**

- **Goal:** Update the board according to the moves read from the file.

- **Instructions:**
  ```python
  def make_move(board, player, row, col):
      if board[row][col] == ' ':
          board[row][col] = player
          return True
      else:
          print(f"Cell ({row}, {col}) is already occupied.")
          return False
  ```

### **Step 4: Check for a Winner**

- **Goal:** Write a function to determine if a player has won after each move.

- **Instructions:**
  ```python
  def check_winner(board, player):
      # Check rows and columns
      for i in range(3):
          if all(board[i][j] == player for j in range(3)):
              return True
          if all(board[j][i] == player for j in range(3)):
              return True
      
      # Check diagonals
      if all(board[i][i] == player for i in range(3)):
          return True
      if all(board[i][2 - i] == player for i in range(3)):
          return True

      return False
  ```

### **Step 5: Run the Game Logic**

- **Goal:** Combine all previous steps to simulate the game from the file.

- **Instructions:**
  ```python
  def play_game(filename):
      board = create_board()
      moves = read_moves(filename)
      
      for player, row, col in moves:
          print(f"{player}'s move: ({row}, {col})")
          valid = make_move(board, player, row, col)
          if not valid:
              print("Invalid move, skipping.")
              continue
          display_board(board)
          
          if check_winner(board, player):
              print(f"Player {player} wins!")
              return
          
      print("Game Over: It's a draw!")

  # Start the game
  play_game('moves.txt')
  ```

---

### **Step 6: Test Your Game**

- **Instructions:**  
  Run the program in your Python IDE or terminal:
  ```
  python tic_tac_toe.py
  ```

- **Expected output (example):**
  ```
  X's move: (0, 0)
  Current Board:
  X| | 
  -----
   | | 
  -----
   | | 
  -----
  O's move: (1, 1)
  Current Board:
  X| | 
  -----
   |O| 
  -----
   | | 
  -----
  X's move: (0, 1)
  Current Board:
  X|X| 
  -----
   |O| 
  -----
   | | 
  -----
  O's move: (1, 0)
  Current Board:
  X|X| 
  -----
  O|O| 
  -----
   | | 
  -----
  X's move: (0, 2)
  Current Board:
  X|X|X
  -----
  O|O| 
  -----
   | | 
  -----
  Player X wins!
  ```