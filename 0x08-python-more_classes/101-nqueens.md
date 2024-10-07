# N queens

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

1. Usage: `nqueens N`
    - If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
2. where N must be an integer greater or equal to 4
    - If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    - If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
3. The program should print every possible solution to the problem
    - One solution per line
    - Format: see example
    - You don’t have to print the solutions in a specific order
4. You are only allowed to import the `sys` module

```
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
```
## How to solve the N Queen problem

Sure! Here’s a detailed step-by-step guide on how to solve the N queens problem using pseudo-code.

### Step 1: Set Up the Program Structure
1. **Create a main function** to contain the logic for the program.

### Step 2: Handle Command-Line Arguments
1. **Check the number of arguments**:
   - If the number of arguments is not equal to 2, print "Usage: nqueens N" and exit with status 1.
  
2. **Convert the argument to an integer**:
   - Try to convert the input argument to an integer.
   - If it fails, print "N must be a number" and exit with status 1.

3. **Check if N is valid**:
   - If N is less than 4, print "N must be at least 4" and exit with status 1.

### Step 3: Set Up the Board Representation
1. **Initialize a board**:
   - Create a list (or array) to represent the board, where each index corresponds to a row and the value at each index corresponds to the column where a queen is placed.

### Step 4: Implement the Backtracking Algorithm
1. **Define a function to print solutions**:
   - Iterate through the board and construct a visual representation of the board with queens and empty spaces, then print it.

2. **Define a function to check if placing a queen is safe**:
   - For each row above the current row, check:
     - If there is a queen in the same column.
     - If there is a queen in the diagonal (both left and right).
   - If no conflicts are found, return true; otherwise, return false.

3. **Define a recursive function to solve N queens**:
   - If all queens are placed (i.e., the current row is equal to N):
     - Print the current board configuration.
   - For each column in the current row:
     - If placing a queen in that column is safe:
       - Place the queen in the board.
       - Recursively attempt to place queens in the next row.
       - Backtrack by removing the queen from the current column.

### Step 5: Combine Everything in the Main Function
1. **Initialize the board**:
   - Create a board list initialized with a sentinel value (e.g., -1) indicating no queens are placed.

2. **Call the solving function** to start placing queens from the first row.

### Pseudo-Code Summary
Here’s a consolidated version of the above steps in pseudo-code:

```pseudocode
FUNCTION main():
    IF number of arguments != 2 THEN
        PRINT "Usage: nqueens N"
        EXIT with status 1
    
    TRY:
        N = CONVERT argument to integer
    EXCEPT ValueError:
        PRINT "N must be a number"
        EXIT with status 1
    
    IF N < 4 THEN
        PRINT "N must be at least 4"
        EXIT with status 1

    INITIALIZE board as list of size N with -1
    CALL solve_nqueens(board, 0, N)

FUNCTION print_solutions(board):
    FOR each row in board:
        CREATE line as list of size N filled with '.'
        SET line[row] to 'Q'
        PRINT line as string

FUNCTION is_safe(board, row, col):
    FOR i from 0 to row-1:
        IF board[i] == col OR
           board[i] - i == col - row OR
           board[i] + i == col + row THEN
            RETURN False
    RETURN True

FUNCTION solve_nqueens(board, row, N):
    IF row == N THEN
        CALL print_solutions(board)
        RETURN

    FOR col from 0 to N-1:
        IF is_safe(board, row, col) THEN
            SET board[row] = col
            CALL solve_nqueens(board, row + 1, N)
```

### Conclusion
This pseudo-code provides a structured approach to solving the N queens problem using backtracking, ensuring all requirements are met, including handling command-line arguments and printing the solutions in the specified format.