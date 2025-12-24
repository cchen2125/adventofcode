import re

def read_data(puzzle_file):
    with open(puzzle_file, "r") as file:
        input_data = file.read()
    return input_data

def get_mul_positions(input_data):
    # find all the index positions of "mul("
    return [match.start() for match in re.finditer("mul\(", input_data)]

def get_do_dont_positions(input_data):
    do_positions = [match.start() for match in re.finditer("do\(\)", input_data)]
    dont_positions = [match.start() for match in re.finditer("don't\(\)", input_data)]
    return do_positions, dont_positions

def check_legit_mul(start_position, input_data):
    end_position = input_data[start_position:].find(')')
    mul_string = input_data[start_position+4:start_position+end_position]

    try:
        values = [int(val) for val in mul_string.split(",")]
    except:
        return 0
    
    if len(values) != 2:
        return 0
    
    return values[0] * values[1]

def get_mul_total(mul_positions, input_data):
    mul_total = 0

    for starting_position in mul_positions:
        mul_total += check_legit_mul(starting_position, input_data)
    
    return mul_total

def get_enabled_mul_total(mul_positions, do_positions, dont_positions, input_data):
    enabled_mul = []

    # mul positions that happen before the first don't
    enabled_mul = enabled_mul + list(filter(lambda x: x < dont_positions[0], mul_positions))

    for do_position in do_positions:
        # find the next don't position
        greater_than_do = lambda val: val > do_position
        dont_position = next((val for val in dont_positions if greater_than_do(val)), len(input_data))
        enabled_mul = enabled_mul + list(filter(lambda x: x > do_position and x < dont_position, mul_positions))
    
    enabled_mul = list(set(enabled_mul))

    return get_mul_total(enabled_mul, input_data)

def main():
    input_data = read_data("puzzle3_2024.txt")
    mul_positions = get_mul_positions(input_data)
    do_positions, dont_positions = get_do_dont_positions(input_data)

    mul_total = get_mul_total(mul_positions, input_data)
    print('Part 1 Answer:', mul_total)
    print('Part 2 answer', get_enabled_mul_total(mul_positions, do_positions, dont_positions, input_data))

if __name__ == "__main__":
    main()