def is_roll_accessible(grid, x, y):
    """
    a roll of toilet paper at index x,y is accessible if there are fewer than four rolls of paper in the eight adjacent positions.
    this function returns True if x,y is a roll of toilet paper and is accessible, False otherwise

    x is along columns, y is along rows, matching how it might look on a graph
    """
    if grid[y][x] != "@":
        return False
    
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

            if grid[new_y][new_x] == "@":
                count += 1
    
    return count < 4

def parse_grid(grid):
    accessible_roll_count = 0
    for i in range(len(grid)):
        row = grid[i]

        for j in range(len(row)):
            is_accessible = is_roll_accessible(grid, j, i)
            if is_accessible:
                accessible_roll_count += 1
    
    print(f"accessible roll count: {accessible_roll_count}")

def main():
    with open("input.txt") as fp:
        grid = fp.read().strip().split()

    parse_grid(grid)

if __name__ == "__main__":
    main()