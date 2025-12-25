import numpy as np

with open('puzzle7.txt', 'r') as file:
    input_data = file.read().splitlines()

diagram = [[c for c in row] for row in input_data]

start_pos = (0, diagram[0].index('S'))
height = len(diagram)
width = len(diagram[0])

split_count = 0

for i in range(1, height):
    for j in range(width):
        if diagram[i-1][j] == 'S' or diagram[i-1][j] == '|':
            if diagram[i][j] == '.':
                diagram[i][j] = '|'
            elif diagram[i][j] == '^':
                if j-1 >= 0:
                    diagram[i][j-1] = '|'
                if j+1 < width:
                    diagram[i][j+1] = '|'
                split_count += 1

print('Part 1', split_count)

diagram = [[c for c in row] for row in input_data]

count_diagram = np.zeros((height, width), dtype=int)
count_diagram[start_pos[0]][start_pos[1]] = 1

for i in range(0, height-1):
    for j in range(width):
        if count_diagram[i][j] != 0:
            if diagram[i+1][j] == '.':
                count_diagram[i+1][j] += count_diagram[i][j]
            elif diagram[i+1][j] == '^':
                if j-1 >= 0:
                    count_diagram[i+1][j-1] += count_diagram[i][j]
                if j+1 < width:
                    count_diagram[i+1][j+1] += count_diagram[i][j]
    

#print(np.array(diagram))
#print(count_diagram)
print('Part 2', np.sum(count_diagram[-1]))



