# Initialize variables
freshness_ranges = []
inventory_ids = []
num_fresh_items = 0

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
    fresh_ranges = merge_ranges(freshness_ranges)

    for item in inventory_ids:
        item_id = int(item.strip())
        if is_fresh(item_id, fresh_ranges):
            num_fresh_items += 1

    print(f"Number of fresh items: {num_fresh_items}")