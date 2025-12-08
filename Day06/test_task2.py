# Read input - preserve all spaces
with open("test_input") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

# Find the maximum width
max_width = max(len(line) for line in lines)

# Pad all lines to the same width
data = []
for line in lines:
    padded_line = line + ' ' * (max_width - len(line))
    data.append(padded_line)

number_of_rows = len(data)
answers = []

# Find where each problem starts and ends (separated by blank columns)
problem_ranges = []
in_problem = False
start_col = 0

for col_idx in range(max_width):
    column = [data[row_idx][col_idx] for row_idx in range(number_of_rows)]
    is_blank = all(c == ' ' for c in column)
    
    if not is_blank and not in_problem:
        # Start of a new problem
        start_col = col_idx
        in_problem = True
    elif is_blank and in_problem:
        # End of current problem
        problem_ranges.append((start_col, col_idx))
        in_problem = False

# Handle last problem if it extends to the end
if in_problem:
    problem_ranges.append((start_col, max_width))

print("Problem ranges:", problem_ranges)

# Process each problem
for start_col, end_col in problem_ranges:
    # Extract the problem block
    problem_width = end_col - start_col
    problem_data = []
    for row_idx in range(number_of_rows):
        problem_data.append(data[row_idx][start_col:end_col])
    
    print(f"\nProblem from col {start_col} to {end_col}:")
    for i, row in enumerate(problem_data):
        print(f"  Row {i}: '{row}'")
    
    # Get operator (last row, rightmost non-space character)
    operator = problem_data[-1].strip()[-1] if problem_data[-1].strip() else None
    print(f"Operator: {operator}")
    
    if not operator or operator not in ['+', '*']:
        continue
    
    # Read digits from right to left, top to bottom
    vertical_numbers = []
    for col_offset in range(problem_width - 1, -1, -1):
        vertical_num_str = ''
        for row_idx in range(number_of_rows - 1):  # Exclude operator row
            char = problem_data[row_idx][col_offset]
            if char != ' ':
                vertical_num_str += char
        
        if vertical_num_str:  # Only add if we got some digits
            print(f"  Column offset {col_offset} (from left): '{vertical_num_str}' -> {int(vertical_num_str)}")
            vertical_numbers.append(int(vertical_num_str))
    
    print(f"Vertical numbers: {vertical_numbers}")
    
    # Calculate result based on operator
    if operator == '+':
        result = sum(vertical_numbers)
        print(f"Sum: {result}")
        answers.append(result)
    elif operator == '*':
        result = 1
        for num in vertical_numbers:
            result *= num
        print(f"Product: {result}")
        answers.append(result)

print("\nAnswers for each problem:", answers)
print("Sum of all answers:", sum(answers))
print("\nExpected: 3263827")
