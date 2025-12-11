def get_total_joltage_for_two(lines):
    total_joltage = 0
    for line in lines:
        # loop over lines to find max
        max_joltage = 0
        for i in range(len(line)):
            for j in range(1, len(line)):
                if i < j:
                    joltage = int(line[i]) * 10 + int(line[j])
                    max_joltage = max(max_joltage, joltage)
        print("---")
        print(f"line: {line}")
        print(f"max joltage: {max_joltage}")
        total_joltage += max_joltage
    
    print(f"total joltage: {total_joltage}")

def find_combos(line: str, position: int, built_so_far: str, digits_left: int):
    if digits_left == 0:
        print(f"found: {built_so_far}")
        return [built_so_far] # built something

    if position > len(line) - digits_left:
        return [] # didn't build anything
    
    # find max digit in range of len(line) - digits_left
    max_digit = 0
    max_digit_position = 0
    for i in range(position, len(line) - digits_left + 1):
        new_max_digit = max(max_digit, int(line[i]))
        if new_max_digit != max_digit:
            max_digit = new_max_digit
            max_digit_position = i
    
    #print(f"max digit: {max_digit}")
    #print(f"at position: {max_digit_position}")
    combos = find_combos(line, max_digit_position+1, built_so_far+str(max_digit), digits_left-1)
    return combos


def find_max_combo(line: str, combo_size: int):
    # take a list of integers in a string, and find the max combo of combo size specified
    start_index = 0
    combos = find_combos(line, start_index, built_so_far="", digits_left=combo_size)
    print(f"combos: {combos}")

    max_combo = max([int(combo) for combo in combos])
    return max_combo


def get_total_joltage_combo(lines):
    # gets total joltage for 12
    # uses combinatorics logic
    total_joltage = 0
    for line in lines:
        print(line)
        joltage = find_max_combo(line, 12)
        total_joltage += joltage
    
    print(f"total joltage: {total_joltage}")

def main():
    with open("input.txt") as fp:
        lines = fp.read().strip().split()

    #get_total_joltage_for_two(lines)
    get_total_joltage_combo(lines)



if __name__ == "__main__":
    main()