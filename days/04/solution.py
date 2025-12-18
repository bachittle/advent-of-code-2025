def adjacent_roll_count(grid, x, y):
    """
    a roll of toilet paper at index x,y has 8 adjacent neighbors
    this function returns the number of adjacent neighbors that are toilet paper rolls @

    x is along columns, y is along rows, matching how it might look on a graph
    """
    if grid[y][x] == ".":
        return None
    
    count = 0

    # check 8 adjacent positions: x-1,y-1; x,y-1; x+1,y-1; x-1,y; (ignore this one: x,y); x+1,y; x-1,y+1; x,y+1; x+1,y+1

    for i in range(3):
        for j in range(3):            
            new_x = x+j-1
            new_y = y+i-1

            if x == new_x and y == new_y:
                continue # only look at adjacent positions

            if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
                continue # ignore outside bounds

            if grid[new_y][new_x] == "@" or grid[new_y][new_x] == "x":
                count += 1
    if count < 4:
        grid[y][x] = "x"

    return count

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def parse_grid(grid):
    total_roll_count = 0
    while True:
        roll_count = 0
        for i in range(len(grid)):
            row = grid[i]

            for j in range(len(row)):
                count = adjacent_roll_count(grid, j, i)
                if count is not None and count < 4:
                    roll_count += 1
        
        #print(f"current roll count: {total_roll_count}")
        #print(f"roll count: {roll_count}")
        if roll_count == 0:
            break

        total_roll_count += roll_count

        # replace all x's with .'s
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'x':
                    grid[i][j] = '.'

    print(f"total roll count: {total_roll_count}")

def main():
    with open("input.txt") as fp:
        grid = [list(line) for line in fp.read().strip().split()]

    parse_grid(grid)

if __name__ == "__main__":
    main()