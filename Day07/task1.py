# Read input
with open("Day07/input") as f:
    rows = [line.strip() for line in f.readlines()]

rows = [list(row) for row in rows]  # Convert to list of lists for mutation
current_beams = 1
beam_positions = [rows[0].index('S')]

for row in range(1, len(rows)):
    print(f"Processing row: {row} with beam positions: {beam_positions}")
    new_beam_positions = []
    for pos in beam_positions:
        if rows[row][pos] == '.':
            rows[row][pos] = '|'
            new_beam_positions.append(pos)
        elif rows[row][pos] == '^':
            current_beams += 1
            new_beam_positions.append(pos - 1)
            new_beam_positions.append(pos + 1)
    beam_positions = list(set(new_beam_positions))


print(f"Total beams reaching the bottom: {current_beams}")
print(f"Total splits: {current_beams - 1}")

# Write output to file
with open("Day07/output", "w") as f:
    for row in rows:
        f.write("".join(row) + "\n")
