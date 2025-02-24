from itertools import permutations

# Function to solve SEND + MORE = MONEY
def solve_crypto_arithmetic():
    # Letters involved in the problem
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

    # Generate all possible permutations of digits for the letters
    for digits in permutations(range(10), len(letters)):
        # Create a mapping from letters to digits
        mapping = dict(zip(letters, digits))

        # Skip if any leading letter is mapped to 0
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Convert words to numbers
        SEND = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
        MORE = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
        MONEY = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y']

        # Check if the equation holds
        if SEND + MORE == MONEY:
            print("Solution found:")
            print(f"SEND = {SEND}")
            print(f"MORE = {MORE}")
            print(f"MONEY = {MONEY}")
            print("Mapping:", mapping)
            return

    print("No solution found.")

# Function to solve ONE + ONE = TWO
def solve_one_one_two():
    # Letters involved in the problem
    letters = ['O', 'N', 'E', 'T', 'W']

    # Generate all possible permutations of digits for the letters
    for digits in permutations(range(10), len(letters)):
        # Create a mapping from letters to digits
        mapping = dict(zip(letters, digits))

        # Skip if any leading letter is mapped to 0
        if mapping['O'] == 0 or mapping['T'] == 0:
            continue

        # Convert words to numbers
        ONE = mapping['O'] * 100 + mapping['N'] * 10 + mapping['E']
        TWO = mapping['T'] * 100 + mapping['W'] * 10 + mapping['O']

        # Check if the equation holds
        if ONE + ONE == TWO:
            print("Solution found:")
            print(f"ONE = {ONE}")
            print(f"TWO = {TWO}")
            print("Mapping:", mapping)
            return

    print("No solution found.")

# Run the solvers
solve_crypto_arithmetic()
solve_one_one_two()
