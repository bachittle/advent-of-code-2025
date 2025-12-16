def parse_grid(grid):
    print(grid[0])

def main():
    with open("basic-input.txt") as fp:
        grid = fp.read().strip().split()

    parse_grid(grid)

if __name__ == "__main__":
    main()