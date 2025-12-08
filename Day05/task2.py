# Initialize variables
freshness_ranges = []
inventory_ids = []

# Read input
with open('Day 5/input', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        if "-" in line:
            start, end = map(int, line.split("-"))
            freshness_ranges.append((start, end))
        elif line == "":
            inventory_ids = lines[i+1:]
            break

# Merge ranges
def merge_ranges(ranges):
    # Sort by start value
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []

    for start, end in ranges:
        if not merged:
            merged.append([start, end])
            continue

        last_start, last_end = merged[-1]

        # Overlap or touching = merge
        if start <= last_end + 1:
            merged[-1][1] = max(last_end, end)
        else:
            # No overlap = add new range
            merged.append([start, end])

    return merged

# Check if fresh
def is_fresh(item_id, ranges):
    for start, end in ranges:
        if start <= item_id <= end:
            return True
    return False

if __name__ == "__main__":
    total_fresh_IDs = 0
    fresh_ranges = merge_ranges(freshness_ranges)

    for r in fresh_ranges:
        total_fresh_IDs += (r[1] - r[0] + 1)

    print(f"Number of fresh items: {total_fresh_IDs}")