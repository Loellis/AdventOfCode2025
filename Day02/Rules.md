# -- PART 1 --

# Valid IDs
- Ranges separated by commas
- Each range has first ID and last ID, separated by a dash
- No leading zeros in IDs

# Invalid IDs
- Made of some sequence of digits repeated twice (55, 6464, 123123, etc.)
- Will be contained in the range (range is inclusive, start and end is included)

# Example
`11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124`

- 11-22 has two invalid IDs, **11** and **22**.
- 95-115 has one invalid ID, **99**.
- 998-1012 has one invalid ID, **1010**.
- 1188511880-1188511890 has one invalid ID, **1188511885**.
- 222220-222224 has one invalid ID, **222222**.
- 1698522-1698528 contains no invalid IDs.
- 446443-446449 has one invalid ID, **446446**.
- 38593856-38593862 has one invalid ID, **38593859**.
- The rest of the ranges contain no invalid IDs.

Adding up all the invalid IDs in this example produces **1227775554**.

# -- PART 2 --
# Invalid IDs
- Invalid if some sequence of digits are repeated at least twice (12341234 = 1234 x 2, 123123123 = 123 x 3, 1212121212 = 12 x 5, 1111111 = 1 x 7)