
# Read input
with open('input_day_1', 'r') as file:
    rotations = file.readlines();

# Initialize variables
position = 50
counter = 0

for rotation in rotations:
    direction, value = rotation[0], int(rotation[1:])

    if direction == 'R':
        position += value
    elif direction == 'L':
        position -= value

    # Wrap around logic (0...99)
    position = position % 100

    # Check for zero condition
    if position == 0:
        counter += 1


print(counter)