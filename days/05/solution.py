import sys

def main():
    with open("input.txt") as fp:
        data = fp.read().strip()

    # split based on double new line
    data = data.split("\n\n")
    if len(data) != 2:
        print("error: data not formatted as expected!")
        sys.exit(1)

    # make the range list in a better format, min at 0, max at 1

    # less pythonic, extra variables and memory allocations
    """ 
    range_list_str = data[0].split()
    range_list = [[0,0]]*len(range_list_str)
    for i in range(len(range_list_str)):
        range_list[i] = [int(x) for x in range_list_str[i].split("-")]
    """

    # more pythonic, probably more efficient too, still hard to read?
    range_list = [[int(x) for x in r.split("-")] for r in data[0].split()]

    # best solution for production: helper function, documenting here for learning
    # range_list = [parse_range(r) for r in data[0].split()]

    # ingredients list can also be in a better format, but easier to do
    ingredients = [int(x) for x in data[1].split()]

    """
    print("range list: ", range_list)
    print("---")
    print("ingredients: ", ingredients)
    """    


    #is_fresh_list = [0]*len(ingredients)
    fresh_count = 0

    # loop over each ingredient, and check if its in the range list
    for i, ing in enumerate(ingredients):
        for r in range_list:
            if r[0] <= ing and ing <= r[1]:
                # ingredient is fresh, mark it as 1
                #is_fresh_list[i] = 1
                fresh_count += 1
                break

    print(f"fresh count: {fresh_count}")


if __name__ == "__main__":
    main()