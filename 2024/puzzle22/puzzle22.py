def read_data(puzzle_file):
    with open(puzzle_file, 'r') as file:
        input_data = file.read().splitlines()
    
    return list(map(int, input_data))

def mix(val1, val2):
    return val1 ^ val2

def prune(val):
    return val % 16777216

def get_next_num(secret_num):
    secret_num = prune(mix(secret_num, secret_num * 64))
    secret_num = prune(mix(secret_num, secret_num // 32))
    secret_num = prune(mix(secret_num, secret_num * 2048))

    return secret_num

def get_final_num(secret_num, num_iters):
    for i in range(num_iters):
        secret_num = get_next_num(secret_num)
    return secret_num

def get_sequence(secret_num, num_iters):
    secret_num_sequence = [secret_num]
    price_sequence = [secret_num % 10]

    for i in range(num_iters):
        secret_num = get_next_num(secret_num)
        secret_num_sequence.append(secret_num)
        price_sequence.append(secret_num % 10)

    price_changes = [price_sequence[i+1] - price_sequence[i] for i in range(len(price_sequence) - 1)]

    return price_sequence, price_changes

def solve_p1(initial_nums):
    num_iters = 2000

    final_total = 0

    for secret_num in initial_nums:
        final_total += get_final_num(secret_num, num_iters)
    
    return final_total

def solve_p2(initial_nums, num_iters = 2000):
    four_change_sequences = {}

    for secret_num in initial_nums:
        price_sequence, price_changes = get_sequence(secret_num, num_iters)
        seen_patterns = []
        for i in range(num_iters - 4):
            four_change_sequence = tuple(price_changes[i:i+4])
            if four_change_sequence not in seen_patterns:
                seen_patterns.append(four_change_sequence)
                if four_change_sequence not in four_change_sequences.keys():
                    four_change_sequences[four_change_sequence] = price_sequence[i+4]
                else:
                    four_change_sequences[four_change_sequence] += price_sequence[i+4]
    
    return max(four_change_sequences.values())

def main():
    puzzle_file = 'puzzle22.txt'
    initial_nums = read_data(puzzle_file)
    print(solve_p1(initial_nums))
    print(solve_p2(initial_nums))

if __name__ == '__main__':
    main()