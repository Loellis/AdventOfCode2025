# Store input to var
with open("input_day_3") as f:
    banks = f.readlines()

# Create bank_max_list
bank_max_list = []

# Define function using a stack to keep the k largest digits (in order)
def max_k_digits(bank, k):
    num_not_used = len(bank) - k
    stack = []

    for battery in bank:
        while num_not_used > 0 and stack and stack[-1] < battery:
            stack.pop()
            num_not_used -= 1
        stack.append(battery)

    # Return the K highest digits
    return "".join(stack[:k])

for bank in banks:
    bank = bank.strip()

    max_joltage = max_k_digits(bank, 12)

    print("For bank: " + bank)
    print("Found max joltage: " + max_joltage)

    bank_max_list.append(max_joltage)

# Sum all values in bank max list
total_joltage = sum([int(max_jolt) for max_jolt in bank_max_list])
average_joltage = total_joltage / len(bank_max_list)
print("Total joltage: " + str(total_joltage))
print("Average joltage: " + str(average_joltage))