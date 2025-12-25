from shapely.geometry import Polygon, box

def read_data(puzzle_file):
    with open(puzzle_file, 'r') as file:
        input_data = file.read().splitlines()
        coords = [tuple(map(int,row.split(','))) for row in input_data]
    
    return coords

def get_rectangles(coords):
    rectangles = []

    for i in range(len(coords)):
        for j in range(i, len(coords)):
            width = abs(coords[i][0] - coords[j][0]) + 1
            height = abs(coords[i][1] - coords[j][1]) + 1
            area = width * height 
            rectangles.append((area, i, j))

    rectangles.sort(reverse=True)
    return rectangles

def get_edges(coords):
    edges = []

    for i in range(len(coords) -1):
        coord1 = coords[i]
        coord2 = coords[i+1]
        edges.append((min(coord1[0], coord2[0]),max(coord1[0], coord2[0]),min(coord1[1], coord2[1]),max(coord1[1], coord2[1])))
    
    edges.append((min(coords[-1][0], coords[0][0]),max(coords[-1][0], coords[0][0]),min(coords[-1][1], coords[0][1]),max(coords[-1][1], coords[0][1])))

    return edges

def shapely_valid_rectange(x1,x2,y1,y2,coords):
    full_shape = Polygon(coords)
    rectangle = box(min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2))

    if full_shape.covers(rectangle):
        return True
    return False

def valid_rectangle(x1,x2,y1,y2,coords,edges):
    minx, maxx, miny, maxy = min(x1,x2), max(x1,x2), min(y1,y2), max(y1,y2)

    for coord in coords:
        if minx < coord[0] < maxx and miny < coord[1] < maxy:
            return False
        
    for edge in edges:
        if maxx > edge[0] and minx < edge[1] and maxy > edge[2] and miny < edge[3]:
            return False
    
    return True



def solve_part1(coords):
    max_area = 0

    for i in range(len(coords)):
        for j in range(i, len(coords)):
            width = abs(coords[i][0] - coords[j][0]) + 1
            height = abs(coords[i][1] - coords[j][1]) + 1
            area = width * height 
            if area > max_area:
                max_area = area

    return max_area 

def solve_part2(coords):
    rectangles = get_rectangles(coords)
    edges = get_edges(coords)

    for rectangle in rectangles:
        x1, y1 = coords[rectangle[1]]
        x2, y2 = coords[rectangle[2]]
        
        if valid_rectangle(x1,x2,y1,y2, coords, edges):
            return rectangle[0]
        
        # if shapely_valid_rectangle(x1,x2,y1,y2,coords):
        #   return rectangle[0]

def main():
    puzzle_file = 'puzzle9.txt'
    coords = read_data(puzzle_file)
    print(solve_part1(coords))
    print(solve_part2(coords))

main()





