def do_math(numbers, operators):
    if numbers and len(numbers[0]) != len(operators):
        raise RuntimeError("invalid input data: length of numbers line doesn't match length of operators")
    
    result_list = []
    for i, op in enumerate(operators):
        result = -1
        for line in numbers:
            if result == -1:
                result = line[i]
            else:
                if op == "*":
                    result *= line[i]
                elif op == "+":
                    result += line[i]
                elif op == "/":
                    if line[i] == 0:
                        raise RuntimeError("division by zero")
                    result /= line[i]
                elif op == "-":
                    result -= line[i]
        
        result_list.append(result)

    return result_list



def main():
    with open("input.txt") as fp:
        data = [x.strip().split() for x in fp.read().strip().split("\n")]
    
    numbers = [[int(x) for x in row] for row in data[:-1]]
    operators = data[-1]

    print(f"numbers: {numbers}")
    print(f"operators: {operators}")

    result = do_math(numbers, operators)
    grand_total = sum(result)

    print(f"result: {result}")
    print(f"grand total: {grand_total}")

if __name__ == "__main__":
    main()