# -- PART 1 --

# Forklifts and rolls of paper
- @-signs are rolls of paper
- A forklift can move a roll of paper if there are fewer than four paper rolls in the eight adjacent positions of the given paper roll

# Example

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

- In the example above the following rolls are eligble for moving (marked by an X)

```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

# Task 1
Find the number of rolls that can be accessed by a forklift.