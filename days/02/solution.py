def parse_range(range_):
    sub_range = range_.split("-")
    start = int(sub_range[0])
    end = int(sub_range[1])

    invalid_added = 0

    for n in range(start, end):
        str_num = str(n)
        if len(str_num) % 2 == 0:
            mid = len(str_num) // 2
            if str_num[:mid] == str_num[mid:]:
                # it's double/invalid, increment counter
                print(f"invalud value: {str_num}")
                invalid_added += n

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