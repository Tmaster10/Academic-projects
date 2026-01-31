# Goal, implete an interative Algorithm to have a queen in each space without clashing with others
def resetBoard(n):
    """Create an empty NxN chessboard."""
    return [[0 for _ in range(n)] for _ in range(n)]

def displayBoard(b):
    """Display the chessboard."""
    for row in b:
        print(row)
    print()

def isSafe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    n = len(board)

    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solveNQueensIterative(n):
    """Find all solutions to the N-Queens problem using an iterative approach."""
    solutions = []  # List to store all valid solutions
    stack = []  # Stack to manage state (row, column)
    board = resetBoard(n)
    row = 0
    col = 0

    while True:
        while row < n:  # Try to place a queen in each row
            # Find a valid column
            while col < n and not isSafe(board, row, col):
                col += 1

            if col < n:  # Found a valid position
                board[row][col] = 1
                stack.append((row, col))  # Save state
                row += 1  # Move to the next row
                col = 0  # Start from the first column in the new row
            else:  # Backtrack
                if not stack:
                    # All possibilities explored
                    return solutions

                # Backtrack to the previous state
                row, col = stack.pop()
                board[row][col] = 0  # Remove the queen
                col += 1  # Try the next column

        # Solution found, add to the list
        solutions.append([row[:] for row in board])

        # Backtrack to find the next solution
        if not stack:
            # All possibilities explored
            return solutions

        row, col = stack.pop()
        board[row][col] = 0  # Remove the queen
        col += 1  # Try the next column

# Main function to run the iterative solver
n = 8  # Change this for different board sizes
solutions = solveNQueensIterative(n)

print(f"Found {len(solutions)} solutions for {n}-Queens problem.")
for idx, solution in enumerate(solutions, start=1):
    print(f"Solution {idx}:")
    displayBoard(solution)
