def read_data(puzzle_file):
    with open(puzzle_file, 'r') as file:
        input_data = file.read().splitlines()
        boxes = [tuple(map(int, row.split(','))) for row in input_data]
    
    return boxes

def get_distances(boxes):
    distances = []

    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            distance = ((boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2)**0.5
            distances.append((distance, i, j))
        
    distances.sort()
    return distances

def update_circuit(box1, box2, circuits, circuit_groups):
    if circuits[box1] == box1 and circuits[box2] == box2:
        circuits[box2] = box1
        for box in circuit_groups[box2]:
            circuits[box] = box1
        
        circuit_groups[box1] = circuit_groups[box1] + circuit_groups[box2]
        del circuit_groups[box2]

        return circuits, circuit_groups
    
    if circuits[box1] == circuits[box2]:
        return circuits, circuit_groups
    
    parent = min(circuits[box1], circuits[box2])
    circuit_groups[parent] = circuit_groups[circuits[box1]] + circuit_groups[circuits[box2]]
    del circuit_groups[max(circuits[box1], circuits[box2])]

    for box in circuit_groups[parent]:
        circuits[box] = parent
    
    return circuits, circuit_groups

def solve_part1(distances, boxes, num_connections):
    circuits = {i: i for i in range(len(boxes))}
    circuit_groups = {i: [i] for i in range(len(boxes))}

    for i in range(num_connections):
        distance, box1, box2 = distances[i]

        circuits, circuit_groups = update_circuit(box1, box2, circuits, circuit_groups)
    
    circuit_sizes = [len(group) for group in circuit_groups.values()]
    circuit_sizes.sort()
    return circuit_sizes[-1] * circuit_sizes[-2] * circuit_sizes[-3]

def solve_part2(distances, boxes):
    circuits = {i: i for i in range(len(boxes))}
    circuit_groups = {i: [i] for i in range(len(boxes))}

    for i in range(len(distances)):
        distance, box1, box2 = distances[i]
        circuits, circuit_groups = update_circuit(box1, box2, circuits, circuit_groups)

        if len(circuit_groups.keys()) == 1:
            return boxes[box1][0] * boxes[box2][0]

def main():
    puzzle_file = 'puzzle8.txt'
    NUM_CONNECT = 1000
    boxes = read_data(puzzle_file)
    distances = get_distances(boxes)
    print(solve_part1(distances, boxes, NUM_CONNECT))
    print(solve_part2(distances, boxes))

if __name__ == "__main__":
    main()