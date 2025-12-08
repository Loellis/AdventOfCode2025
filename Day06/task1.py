# Read input
with open("Day06/input") as f:
    # Remove multiple whitespaces and split string into a list
    data = [line.strip().split() for line in f.readlines()]

number_of_problems = len(data[0])
answers = []

for i in range(number_of_problems):
    # Last line (bottom row) contains the operator for each problem
    operator = data[-1][i]

    if operator == '+':
        # Sum all numbers in the current column except the last line
        column_sum = sum(int(data[j][i]) for j in range(len(data) - 1))
        answers.append(column_sum)
    elif operator == '*':
        # Multiply all numbers in the current column except the last line
        product = 1
        for j in range(len(data) - 1):
            product *= int(data[j][i])
        answers.append(product)


print("Sum of all answers:", sum(answers))
