def read_data(puzzle_file):
    with open(puzzle_file, "r") as file:
        input_data = file.read()
    
    keys = []
    locks = []

    for item in input_data.split('\n\n'):
        if item[:5] == '#####':
            full_lock = [[c for c in row] for row in item.split('\n')]
            locks.append(full_lock[1:-1])
        if item[:5] == '.....':
            full_key = [[c for c in row] for row in item.split('\n')]
            keys.append(full_key[1:-1])

    return keys, locks

def get_pin_heights(item):
    pin_heights = [0] * 5

    for row in item:
        for i in range(5):
            if row[i] == '#':
                pin_heights[i] += 1
    
    return pin_heights

def check_lock_key_match(key, lock):
    combined_heights = [key_height + lock_height for key_height, lock_height in zip(key, lock)]
    if any(height > 5 for height in combined_heights):
        return False
    return True 

def count_lock_key_matches(keys, locks):
    key_pin_heights = [get_pin_heights(key) for key in keys]
    lock_pin_heights = [get_pin_heights(lock) for lock in locks]

    num_matches = 0

    for key in key_pin_heights:
        for lock in lock_pin_heights:
            if check_lock_key_match(key, lock):
                num_matches += 1
    
    return num_matches

def main():
    puzzle_file = 'puzzle25.txt'
    keys, locks = read_data(puzzle_file)

    print('Part 1 answer', count_lock_key_matches(keys, locks))

if __name__ == "__main__":
    main()