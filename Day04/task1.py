# Read input
with open("Day 4/input", "r") as file:
    data = file.readlines()

# Create a list of lists
grid = [list(line.strip()) for line in data]

number_of_eligible_rolls = 0

# Iterate over each row
for i in range(len(grid)):
    # Iterate over each column
    for j in range(len(grid[i])):
        # Check if the current cell is "@", if not, skip
        if grid[i][j] != "@":
            continue
        
        # Check adjacent cells
        adjacent_at_count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if adjacent_at_count >= 4:
                    break
                if di == 0 and dj == 0:
                    continue  # Skip the current cell itself
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                    if grid[ni][nj] == "@":
                        adjacent_at_count += 1

        if adjacent_at_count < 4:
            number_of_eligible_rolls += 1

# Print result
print(number_of_eligible_rolls)