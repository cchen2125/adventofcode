def read_data(puzzle_file):
    with open(puzzle_file, "r") as file:
        input_data = file.read()
    
    split_input = input_data.split('\n\n')
    rules, updates = split_input[0], split_input[1]

    rules = rules.split('\n')
    updates = [[int(val) for val in update.split(',')] for update in updates.split('\n')]

    return rules, updates

def check_valid_update(update, rules):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            disqualifying_rule = f'{update[j]}|{update[i]}'
            if disqualifying_rule in rules:
                return False
    return True

def get_middle_val(update):
    return update[len(update) // 2]

def solve_part_1(rules, updates):
    valid_middle_val_sum = 0

    for update in updates:
        if check_valid_update(update, rules):
            valid_middle_val_sum += get_middle_val(update)
    
    return valid_middle_val_sum

def reorder(update, rules):
    if check_valid_update(update, rules):
        return update
    
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            disqualifying_rule = f'{update[j]}|{update[i]}'
            if disqualifying_rule in rules:
                temp = update[i]
                update[i] = update[j]
                update[j] = temp
    return reorder(update, rules)

def solve_part_2(rules, updates):
    invalid_middle_val_sum = 0
    for update in updates:
        if not check_valid_update(update, rules):
            fixed_update = reorder(update, rules)
            invalid_middle_val_sum += get_middle_val(fixed_update)
    return invalid_middle_val_sum

def main():
    puzzle_file = 'puzzle5.txt'
    rules, updates = read_data(puzzle_file)

    print(f'Part 1 answer: {solve_part_1(rules, updates)}')
    print(f'Part 2 answer: {solve_part_2(rules, updates)}')

if __name__ == "__main__":
    main()