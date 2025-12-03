import time

def is_repeating(num: str) -> bool:
    if len(num) % 2 != 0:
        return False
    half = len(num) // 2
    return num[:half] == num[half:]

if __name__ == "__main__":
    sum_of_invalid_IDs = 0

    with open("input_day_2", "r") as file:
        ranges = [line.strip() for line in file.read().split(",")]
        
    for r in ranges:
        start, end = map(int, r.split("-"))
        for number in range(start, end + 1):
            if is_repeating(str(number)):
                sum_of_invalid_IDs += number

    print(f"Sum of all invalid IDs: {sum_of_invalid_IDs}")

