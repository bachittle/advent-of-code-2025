def main():
    with open("input.txt") as fp:
        data = fp.read().strip().split()

    # find s location in first line
    s_location = data[0].find("S")

    print(f"data size: {len(data)}")

    print(f"S located at index {s_location}")

    total_splits = 0
    locations = [s_location]
    print(f"total locations: {locations}")

    for i in range(1, len(data)):
        split_locations = []
        for j, c in enumerate(data[i]):
            if c == "^":
                split_locations.append(j)

        for split_location in split_locations:
            if split_location in locations:
                #print(f"found split at row {i} and location {split_location}")
                total_splits += 1
                # remove that location and add new locations at +1/-1
                locations.remove(split_location)

                if split_location >= 1:
                    locations.append(split_location - 1)
                if split_location < len(data[i]) - 1:
                    locations.append(split_location + 1)
                
                # remove duplicates
                locations = list(set(locations))
                #print(locations)

    print("---")
    print(f"total splits: {total_splits}")

if __name__ == "__main__":
    main()