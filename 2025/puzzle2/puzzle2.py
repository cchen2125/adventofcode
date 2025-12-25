with open("puzzle2.txt", "r") as file:
    input_data = file.read()
    id_ranges = [list(map(int, id_range.split('-'))) for id_range in input_data.split(',')]

invalid_part1 = 0

for id_range in id_ranges:
    for val in range(id_range[0], id_range[1]+1):
        str_val = str(val)
        num_digits = len(str_val)

        if num_digits % 2 == 0:
            # if str_val[:num_digits // 2] == str_val[num_digits // 2:]:
            if str_val[:num_digits // 2] * 2 == str_val:
                invalid_part1 += val

print('Part 1', invalid_part1)

invalid_part2 = 0

for id_range in id_ranges:
    for val in range(id_range[0], id_range[1]+1):
        str_val = str(val)
        num_digits = len(str_val)
        for sequence_length in range(1, num_digits // 2 + 1):
            if num_digits % sequence_length == 0:
                # subsequences = [str_val[i:i+sequence_length] for i in range(0, num_digits, sequence_length)]
                # if len(set(subsequences)) == 1:
                if str_val[:sequence_length] * (num_digits // sequence_length) == str_val:
                    invalid_part2 += val
                    break

print('Part 2', invalid_part2)