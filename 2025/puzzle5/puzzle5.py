with open('puzzle5.txt', 'r') as file:
    input_data = file.read().split('\n\n')
    fresh_ranges, ids = input_data[0].split('\n'), input_data[1].split('\n')

def solve_p1(fresh_ranges, ids):
    fresh_list = []

    for id in ids:
        for fresh_range in fresh_ranges:
            fresh_range = list(map(int, fresh_range.split('-')))
            if fresh_range[0] <= int(id) <= fresh_range[1]:
                fresh_list.append(id)

    fresh_set = set(fresh_list)

    return len(fresh_set)

def solve_p2(fresh_ranges, ids):
    all_fresh_num = 0

    fresh_ranges = [list(map(int, fresh_range.split('-'))) for fresh_range in fresh_ranges]

    fresh_ranges.sort()

    last_fresh_id = 0

    for fresh_range in fresh_ranges:
        if fresh_range[1] <= last_fresh_id:
            pass
        elif fresh_range[0] <= last_fresh_id and fresh_range[1] >= last_fresh_id:
            all_fresh_num += fresh_range[1] - last_fresh_id
        elif fresh_range[0] > last_fresh_id:
            all_fresh_num += fresh_range[1] - fresh_range[0] + 1
        last_fresh_id = max(fresh_range[1], last_fresh_id)

    return all_fresh_num

print('Part 1', solve_p1(fresh_ranges, ids))
print('Part 2', solve_p2(fresh_ranges, ids))