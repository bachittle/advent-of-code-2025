import math

def get_euclidean_distance(point0, point1):
    """
    point0 = [x0,y0,z0]
    point1 = [x1,y1,z1]
    
    distance = sqrt((x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2)
    """
    x0 = point0[0]
    y0 = point0[1]
    z0 = point0[2]

    x1 = point1[0]
    y1 = point1[1]
    z1 = point1[2]

    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2)

def find_two_closest_points(coords, connected_list) -> tuple[int, int]:
    """
    use Euclidean distance to find two closest points
    coords = [[x0,y0,z0], [x1,y1,z1], [x2,y2,z2], ...]
    check each point and get a distance
    distance_0_1 = sqrt((x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2)
    distance_0_2 = sqrt((x0 - x2)**2 + (y0 - y2)**2 + (z0 - z2)**2)
    ...

    get min distance, thats two closest points
    returns the indices of those 2 closest points
    """

    min_distance = None
    point0_index = -1
    point1_index = -1

    for i in range(len(coords)):
        #print(f"point i: {coords[i]}")

        for j in range(i+1, len(coords)):
            #print(f"point j: {coords[j]}")

            if (i,j) in connected_list:
                print(f"skipping {(i,j)} due to already being connected")
                continue

            distance = get_euclidean_distance(coords[i], coords[j])
            #print(f"distance: {distance}")

            if min_distance is None or distance < min_distance:
                min_distance = distance
                point0_index = i
                point1_index = j
    
    return (point0_index, point1_index)


def main():
    with open("basic-input.txt") as fp:
        data = fp.read().strip().split()

    # normalize coords to integer arrays of size 3 (x,y,z)
    coords = [[int(x) for x in coord.split(",")] for coord in data]
    #print(coords)

    connected_list = []


    for i in range(11):
        point0_index, point1_index = find_two_closest_points(coords, connected_list)
        print(f"two closest points: {coords[point0_index]}, {coords[point1_index]}")
        print(f"two closest points indices: {point0_index}, {point1_index}")

        connected_list.append((point0_index, point1_index))
        print(f"connected list: {connected_list}")
        print("---")

    
        
    

if __name__ == "__main__":
    main()