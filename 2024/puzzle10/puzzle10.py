def read_data(puzzle_file):
    with open(puzzle_file, "r") as file:
        input_data = file.read().splitlines()
        topo_map = [[int(c) for c in row] for row in input_data]
    
    return topo_map

def find_trailheads(topo_map):
    trailheads = []
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j] == 0:
                trailheads.append((i,j))
    
    return trailheads

def calc_trailhead_score(trailhead, topo_map):
    map_height = len(topo_map)
    map_width = len(topo_map[0])

    reachable_trail_ends = []
    partial_trails = [[trailhead]]

    while len(partial_trails) != 0:
        partial_trail = partial_trails.pop()
        last_x, last_y = partial_trail[-1][0], partial_trail[-1][1]
        last_level = topo_map[last_x][last_y]

        # if the partial trail is a complete trail, add it to reachable trail ends
        if last_level == 9:
            if (last_x, last_y) not in reachable_trail_ends:
                reachable_trail_ends.append((last_x, last_y))
        
        # check for viable next steps
        if last_x > 0:
            if topo_map[last_x-1][last_y] == last_level + 1:
                partial_trails.append(partial_trail + [(last_x-1, last_y)])
        if last_y > 0:
            if topo_map[last_x][last_y-1] == last_level + 1:
                partial_trails.append(partial_trail + [(last_x, last_y - 1)])
        if last_x < map_height - 1:
            if topo_map[last_x+1][last_y] == last_level + 1:
                partial_trails.append(partial_trail + [(last_x+1, last_y)])
        if last_y < map_width - 1:
            if topo_map[last_x][last_y+1] == last_level + 1:
                partial_trails.append(partial_trail + [(last_x, last_y +1)])
    
    return len(reachable_trail_ends)

def calc_trailhead_rating(trailhead, topo_map):
    map_height = len(topo_map)
    map_width = len(topo_map[0])

    rating = 0
    partial_trails = [[trailhead]]

    while len(partial_trails) != 0:
        partial_trail = partial_trails.pop()
        last_x, last_y = partial_trail[-1][0], partial_trail[-1][1]
        last_level = topo_map[last_x][last_y]

        # if the partial trail is a complete trail, add it to reachable trail ends
        if last_level == 9:
            rating += 1
        
        # check for viable next steps
        if last_x > 0:
            if topo_map[last_x-1][last_y] == last_level + 1:
                partial_trails.append(partial_trail + [(last_x-1, last_y)])
        if last_y > 0:
            if topo_map[last_x][last_y-1] == last_level + 1:
                partial_trails.append(partial_trail + [(last_x, last_y - 1)])
        if last_x < map_height - 1:
            if topo_map[last_x+1][last_y] == last_level + 1:
                partial_trails.append(partial_trail + [(last_x+1, last_y)])
        if last_y < map_width - 1:
            if topo_map[last_x][last_y+1] == last_level + 1:
                partial_trails.append(partial_trail + [(last_x, last_y +1)])
    
    return rating

def main():
    topo_map = read_data("puzzle10.txt")
    trailheads = find_trailheads(topo_map)
    trailhead_scores = [calc_trailhead_score(trailhead, topo_map) for trailhead in trailheads]
    print('Part 1 answer', sum(trailhead_scores))
    print('Part 2 answer', sum([calc_trailhead_rating(trailhead, topo_map) for trailhead in trailheads]))

if __name__ == "__main__":
    main()