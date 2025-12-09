# Read input
with open("Day07/input") as f:
    rows = [line.strip() for line in f.readlines()]

rows = [list(row) for row in rows]  # Convert to list of lists for mutation

# Dictionary to count how many paths reach each position
path_counts = {rows[0].index('S'): 1}

for row in range(1, len(rows)):
    print(f"Processing row: {row} with path counts: {path_counts}")
    new_path_counts = {}
    
    for pos, count in path_counts.items():
        if rows[row][pos] == '.':
            rows[row][pos] = '|'
            new_path_counts[pos] = new_path_counts.get(pos, 0) + count
        elif rows[row][pos] == '^':
            # Split: each path becomes 2 paths
            new_path_counts[pos - 1] = new_path_counts.get(pos - 1, 0) + count
            new_path_counts[pos + 1] = new_path_counts.get(pos + 1, 0) + count
    
    path_counts = new_path_counts

total_paths = sum(path_counts.values())
print(f"Total paths reaching the bottom: {total_paths}")

# Write output to file
with open("Day07/output", "w") as f:
    for row in rows:
        f.write("".join(row) + "\n")
