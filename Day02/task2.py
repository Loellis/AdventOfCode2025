import time

def is_repeating(num: str) -> bool:
    for chunk_size in range(1, len(num) // 2 + 1):
        if len(num) % chunk_size == 0:
            chunks = [num[i:i + chunk_size] for i in range(0, len(num), chunk_size)]
            if all(chunk == chunks[0] for chunk in chunks):
                return True
    return False

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

