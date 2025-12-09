def load_input(filename: str):
    with open(filename) as fp:
        return fp.read().strip().splitlines()

def turn_dial(dial_input: int, instruction: str):
    letter = instruction[0]
    number = int(instruction[1:])

    zero_count = 0

    if letter == "L":
        dial_input = (dial_input - number) % 100
        zero_count = (dial_input + number) // 100
    elif letter == "R":
        dial_input = (dial_input + number) % 100
        if dial_input == 0:
            zero_count = number // 100
        else:
            zero_count = ((100 - dial_input) + number) // 100
    
    return dial_input, zero_count

def main():
    import sys

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        return

    dial_instructions = load_input(sys.argv[1])
    print(dial_instructions[0])

    dial_position = 50
    zero_count_total = 0

    for instruction in dial_instructions:
        dial_output, zero_count = turn_dial(dial_position, instruction)
        #print(f"initial dial position: {dial_position}, instruction: {instruction}, dial output: {dial_output}")
        dial_position = dial_output
        zero_count_total += zero_count

    print(f"final position: {dial_position}")
    print(f"zero count: {zero_count_total}")


if __name__ == "__main__":
    main()