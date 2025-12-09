# Teleportation trouble

- Start from the first line at the position "S"
- Make a downward line (|) in the same position (column index) if the current line contains empty space (.)
- If current column position contains a splitter (^) create a downward line on each side of the (^), then both of these lines continue downward

How many times will the beam have been split after reaching the last line.

## --- PART TWO ---

Now count all the possible paths from the top to the bottom.