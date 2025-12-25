import networkx as nx

with open('puzzle8.txt', 'r') as file:
    input_data = file.read().splitlines()
    boxes = [(tuple(map(int,row.split(',')))) for row in input_data]

distances_dict = {}

for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        distance = ((boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2]) **2)**0.5
        distances_dict[distance] = (i,j)

distances_list = list(distances_dict.keys())
distances_list.sort()

NUM_CONNECT = 1000

G = nx.Graph()

for i in range(NUM_CONNECT):
    distance = distances_list[i]
    G.add_edge(distances_dict[distance][0], distances_dict[distance][1])

components = list(nx.connected_components(G))
circuit_sizes = [len(c) for c in components]
circuit_sizes.sort()

print(circuit_sizes[-1] * circuit_sizes[-2] * circuit_sizes[-3])

NUM_BOXES = len(boxes)

for i in range(NUM_CONNECT+1, len(distances_list)):
    distance = distances_list[i]
    G.add_edge(distances_dict[distance][0], distances_dict[distance][1])
    if len(list(nx.connected_components(G))[0]) == NUM_BOXES:
        box1 = distances_dict[distance][0]
        box2 = distances_dict[distance][1]
        print(boxes[box1][0] * boxes[box2][0])
        break