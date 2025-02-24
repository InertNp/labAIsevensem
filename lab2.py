from itertools import permutations

def solve_crypto_arithmetic():
    # Letters involved in the problem
    letters = ['T', 'W', 'O', 'F', 'U', 'R']

    # Generate all possible permutations of digits for the letters
    for digits in permutations(range(10), len(letters)):
        # Create a mapping from letters to digits
        mapping = dict(zip(letters, digits))

        # Skip if any leading letter is mapped to 0
        if mapping['T'] == 0 or mapping['F'] == 0:
            continue

        # Convert words to numbers
        TWO = mapping['T'] * 100 + mapping['W'] * 10 + mapping['O']
        FOUR = mapping['F'] * 1000 + mapping['O'] * 100 + mapping['U'] * 10 + mapping['R']

        # Check if the equation holds
        if TWO + TWO == FOUR:
            print("Solution found:")
            print(f"TWO = {TWO}")
            print(f"FOUR = {FOUR}")
            print("Mapping:", mapping)
            return

    print("No solution found.")

# Run the solver
solve_crypto_arithmetic()


def is_safe(board, row, col):
    # Check if a queen can be placed at (row, col)
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens(board, row):
    # Base case: All queens are placed
    if row == 8:
        print("Solution:", board)
        return True

    # Try placing a queen in each column of the current row
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # Place the queen
            if solve_queens(board, row + 1):  # Recur for the next row
                return True
            board[row] = -1  # Backtrack

    return False

# Initialize the board (list of 8 elements, -1 means no queen is placed)
board = [-1] * 8

# Solve the problem
solve_queens(board, 0)
