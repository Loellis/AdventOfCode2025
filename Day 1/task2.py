with open('input_day_1', 'r') as file:
    rotations = file.readlines()

position = 50
counter = 0

for rotation in rotations:
    direction, value = rotation[0], int(rotation[1:].strip())

    if direction == 'R':
        counter += (position + value) // 100
        position = (position + value) % 100
    elif direction == 'L':
        if (position - value) < 0:
            counter += abs((100 + position - value) // 100)
            if position != 0:
                counter += 1
        position = (position - value) % 100
        if position == 0:
            counter += 1

print(counter)