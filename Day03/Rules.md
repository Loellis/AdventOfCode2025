# -- PART 1 --

## Joltage, batteries and banks
- Each has a joltage rating from 1 to 9
- Batteries are arranged into banks (each line in the input is a bank)
- Within each bank you need to turn on **exactly two** batteries
- The joltage the bank produces is equal to the number formed by the digits of the batteries that are turned on
- Batteries cannot be rearranged

## Examples

**Input**
```
987654321111111
811111111111119
234234234234278
818181911112111
```

- In **98**7654321111111, you can make the largest joltage possible, **98**, by turning on the first two batteries.
- In **8**1111111111111**9**, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing **89** jolts.
- In 2342342342342**78**, you can make **78** by turning on the last two batteries (marked 7 and 8).
- In 818181**9**1111**2**111, the largest joltage you can produce is **92**.

## Task 1
Find the sum of the maximum joltage possible from each bank.

# -- PART 2 --

## Joltage, batteries and banks
- Turn on exactly 12 batteries rather than 2 per bank