import numpy as np
import math

with open('puzzle6.txt', 'r') as file:
    input_data = file.read().splitlines()

problem_grid = [[val for val in row.split(' ') if val.strip()] for row in input_data]
val_grid = np.array([[val for val in row] for row in input_data])

def solve_p1(problem_grid):
    operations = problem_grid.pop(-1)
    problem_grid = np.array(problem_grid).astype(int)

    answer_sum = 0

    for i in range(len(operations)):
        if operations[i] == '*':
            answer_sum += math.prod(problem_grid[:,i])
        if operations[i] == '+':
            answer_sum += np.sum(problem_grid[:,i])

    return answer_sum

def solve_p2(val_grid):

    p2_sum = 0

    current_values = []

    for i in range(val_grid.shape[1]):
        if list(val_grid[:,i]) == [' '] * val_grid.shape[0]:
            #print(current_values)
            if operation == '+':
                p2_sum += sum(current_values)
            if operation == '*':
                p2_sum += math.prod(current_values)
            current_values = []
        else:
            if val_grid[:,i][-1] in ['+', '*']:
                operation = val_grid[:,i][-1]
            
            current_values.append(int(''.join(list(val_grid[:-1,i])).strip()))

    if operation == '+':
        p2_sum += sum(current_values)
    if operation == '*':
        p2_sum += math.prod(current_values)

    return p2_sum

print('Part 1', solve_p1(problem_grid))
print('Part 2', solve_p2(val_grid))
    