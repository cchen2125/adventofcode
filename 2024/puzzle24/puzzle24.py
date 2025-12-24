def read_data(puzzle_file):
    with open(puzzle_file, 'r') as file:
        input_data = file.read()
        input_values, gates = input_data.split('\n\n')

        input_values = {wire: int(val) for wire, val in [row.split(': ') for row in input_values.split('\n')]}

        gates = [{'inputs': (row[0], row[2]), 'operation': row[1], 'output': row[-1]} for row in [gate.split(' ') for gate in gates.split('\n')]]

        return input_values, gates
    
def get_z_outputs(input_values, gates):
    z_outputs = []
    input_values_copy = {wire:val for wire, val in input_values.items()}
    gates_queue = [gate for gate in gates]

    while len(gates_queue) != 0:
        gate = gates_queue.pop(0)
        input1, input2 = gate['inputs']

        if input1 not in input_values_copy.keys() or input2 not in input_values_copy.keys():
            gates_queue.append(gate)
            continue

        if gate['operation'] == 'AND':
            output_val = input_values_copy[input1] & input_values_copy[input2]
        elif gate['operation'] == 'OR':
            output_val = input_values_copy[input1] | input_values_copy[input2]
        else:
            output_val = input_values_copy[input1] ^ input_values_copy[input2]
        
        if gate['output'][0] == 'z':
            z_outputs.append((gate['output'], output_val))
            continue

        input_values_copy[gate['output']] = output_val
    
    z_outputs.sort()
    return z_outputs

def wires_to_bit_int(sorted_outputs):
    binary_num = ''.join([str(output[1]) for output in list(reversed(sorted_outputs))])
    return int(binary_num, 2)

def solve_p1(input_values, gates):
    z_ouputs = get_z_outputs(input_values, gates)
    return wires_to_bit_int(z_ouputs)

def main():
    puzzle_file = 'puzzle24.txt'
    input_values, gates = read_data(puzzle_file)

    print(solve_p1(input_values, gates))

    # x_inputs = [(wire, val) for wire, val in input_values.items() if wire[0] == 'x']
    # y_inputs = [(wire, val) for wire, val in input_values.items() if wire[0] == 'y']

    # correct_answer = wires_to_bit_int(x_inputs) + wires_to_bit_int(y_inputs)
    # print(bin(correct_answer))
    # print(bin(solve_p1(input_values, gates)))

main()