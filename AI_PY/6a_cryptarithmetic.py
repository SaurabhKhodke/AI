from itertools import permutations
import re # Import the re module for robust splitting

def solve_cryptarithmetic(puzzle):
    # Ensure the puzzle contains an '=' sign
    if '=' not in puzzle:
        print("Error: Puzzle must contain an '=' sign.")
        return None

    # Extract all unique letters
    # Use regex to find all sequences of letters
    letters = sorted(set(char for word in re.findall(r'[A-Za-z]+', puzzle) for char in word if char.isalpha()))

    if len(letters) > 10:
        print("Error: Too many unique letters (more than 10) for base-10 digits.")
        return None

    # Split puzzle into left and right of '='
    try:
        left_expr, right_expr = puzzle.split('=')
        # Use regex to find terms (sequences of letters) in the left expression
        left_terms = re.findall(r'[A-Za-z]+', left_expr)
        right_term = right_expr.strip()
        # Check if the right term is a valid word (contains only letters)
        if not re.fullmatch(r'[A-Za-z]+', right_term):
             print(f"Error: Invalid term found on the right side of '=': '{right_term}'.")
             return None
        all_terms = left_terms + [right_term]

    except ValueError:
        print("Error: Invalid puzzle format. Make sure there is exactly one '=' sign.")
        return None


    # First letters cannot be zero
    first_letters = {term[0] for term in all_terms if term} # Handle empty terms just in case

    # Try all possible digit assignments
    for digits in permutations(range(10), len(letters)):
        # Create digit mapping
        mapping = {letters[i]: digit for i, digit in enumerate(digits)}

        # Skip if any first letter is assigned 0
        if any(mapping[letter] == 0 for letter in first_letters):
             continue

        # Evaluate all terms
        term_values = {}
        valid_mapping = True

        for term in all_terms:
            num = 0
            for char in term:
                # Ensure the character is in the mapping (should be if letters extraction is correct)
                if char not in mapping:
                    valid_mapping = False
                    break
                num = num * 10 + mapping[char]
            if not valid_mapping:
                break # Exit inner loop if mapping is invalid for a character
            term_values[term] = num

        if not valid_mapping:
            continue # Skip this permutation if a character was not in the mapping

        # Check if equation holds
        left_sum = sum(term_values[term] for term in left_terms)

        if left_sum == term_values[right_term]:
            return term_values

    return None  # No solution found

# Example usage with user input
if __name__ == "__main__":
    print("--- Cryptarithmetic Puzzle Solver ---")
    print("Enter your puzzle (e.g., SEND + MORE = MONEY)")
    user_puzzle = input("Puzzle: ")

    # Clean up the input slightly (remove extra spaces around +, =, etc.)
    user_puzzle = user_puzzle.replace(" ", "").replace("+", " + ").replace("=", " = ").strip()

    solution = solve_cryptarithmetic(user_puzzle)

    if solution:
        print("\nSolution found:")
        # Reconstruct the terms in the original input order for output
        try:
             left_expr, right_expr = user_puzzle.split('=')
             # Use regex to find terms to maintain original ordering from input
             terms_in_order = re.findall(r'[A-Za-z]+', user_puzzle)

             # Format the output as requested
             output = ", ".join(f"{term}: {solution[term]}" for term in terms_in_order if term in solution)
             print(output)
        except ValueError:
             # Fallback if splitting by '=' fails after cleaning
             print("Could not format output due to parsing error.")
             print(solution) # Print the raw solution dictionary


    else:
        print("\nNo solution exists for this puzzle.")