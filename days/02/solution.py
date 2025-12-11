def parse_range(range_):
    sub_range = range_.split("-")
    start = int(sub_range[0])
    end = int(sub_range[1])

    invalid_added = 0

    for n in range(start, end+1):
        str_num = str(n)
        for i in range(1, len(str_num) // 2 + 1):
            rep = len(str_num) // i
            #print(f"{str_num[:i]} * {rep} => {str_num[:i] * rep} => {str_num}?")
            result = str_num[:i] * rep
            if result == str_num:
                invalid_added += n
                break

    return invalid_added
    

def main():
    with open("input.txt") as fp:
        data = fp.read().strip()

    ranges = data.split(",")

    invalid_added = 0
    for range in ranges:
        invalid_added += parse_range(range)
        print(f"invalid count: {invalid_added}")
        


    print(f"total invalid count: {invalid_added}")

if __name__ == "__main__":
    main()