
# Store input to var
with open("input_day_3") as f:
    banks = f.readlines()

# Create bank_max_list
bank_max_list = []

# Iterate over each bank
for bank in banks:
    bank = bank.strip()
    current_max = 0
    current_max_index = -1
    first_max = 0
    second_max = 0

    # First iteration, find first max
    for index_of_battery in range(0, len(bank)):
        if int(current_max) < int(bank[index_of_battery]) and index_of_battery != len(bank) - 1: # Make sure largest num is not the last digit
            current_max = bank[index_of_battery]
            current_max_index = index_of_battery

    first_max = current_max
    # First max found, now find second max, starting from position after first max
    for index_of_battery in range(current_max_index + 1, len(bank)):
        if int(second_max) < int(bank[index_of_battery]): 
            second_max = bank[index_of_battery]
    
    print("For bank: " + bank)
    print("First max: " + str(first_max))
    print("Second max: " + str(second_max))
    print("Appending to bank max list: " + str(first_max) + str(second_max))

    bank_max_list.append(str(first_max) + str(second_max))

# Sum all values in bank max list
total_joltage = sum([int(max_jolt) for max_jolt in bank_max_list])
average_joltage = total_joltage / len(bank_max_list)
print("Total joltage: " + str(total_joltage))
print("Average joltage: " + str(average_joltage))