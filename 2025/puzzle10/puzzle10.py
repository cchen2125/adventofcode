
import numpy as np
from scipy.optimize import milp, LinearConstraint

def read_data(puzzle_file):
    with open(puzzle_file, 'r') as file:
        input_data = [row.split() for row in file.read().splitlines()]
        machines = [
            {
                'diagram': [0 if light == '.' else 1 for light in machine[0].strip('[]')], 
                'buttons': [list(map(int, button.strip('()').split(','))) for button in machine[1:-1]], 
                'joltage': [int(i) for i in machine[-1].strip('}{').split(',')]
            } 
        for machine in input_data]
        
    return machines

def buttons_to_matrix(machine):
    num_lights = len(machine['diagram'])
    num_buttons = len(machine['buttons'])
    matrix = np.zeros((num_lights, num_buttons), dtype=int)
    for i in range(num_buttons):
        for light in machine['buttons'][i]:
            matrix[light][i] = 1

    return matrix

def find_min_buttons(machine):
    button_matrix = buttons_to_matrix(machine)

    combos = []
    num_buttons = button_matrix.shape[1]
    min_buttons = num_buttons

    for i in range(2**num_buttons):
        combos.append(bin(i)[2:].zfill(num_buttons))
    press_vectors = [[int(bit) for bit in combo] for combo in combos]
    
    for press_vector in press_vectors:
        result = np.dot(button_matrix, press_vector) % 2
        if list(result) == machine['diagram']:
            if np.sum(press_vector) < min_buttons:
                min_buttons = np.sum(press_vector)
    
    return min_buttons

def solve_p1(machines):
    total_buttons = 0

    for machine in machines:
        total_buttons += find_min_buttons(machine)
    
    return total_buttons

def solve_p2(machines):
    total_buttons = 0

    for machine in machines:
        button_matrix = buttons_to_matrix(machine)

        num_buttons = len(machine['buttons'])

        integrality = np.ones(num_buttons)
        lower_bound = np.array(machine['joltage'])
        upper_bound = np.array(machine['joltage'])
        
        constraints = LinearConstraint(button_matrix, lower_bound, upper_bound)

        total_buttons += np.sum(milp(c=np.ones(num_buttons), integrality=integrality, constraints=constraints).x)

    return int(total_buttons)

def main():
    puzzle_file = 'puzzle10_example.txt'
    machines = read_data(puzzle_file)
    
    print(solve_p1(machines))
    print(solve_p2(machines))

main()