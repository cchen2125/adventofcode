import functools

def read_data(puzzle_file):
    with open(puzzle_file, 'r') as file:
        input_data = file.read().splitlines()
    
    attachments = {row.split()[0].strip(':'): row.split()[1:] for row in input_data}
    return attachments

def get_num_paths_opt(attachments, start, end):
    @functools.cache
    def dfs(node, end):
        if node == end:
            return 1
        if node == 'out':
            return 0
        
        total = 0
        for output in attachments[node]:
            total += dfs(output, end)
        return total
    
    return dfs(start, end)

def get_num_paths(attachments, start, end):
    partial_paths = [[start]]

    num_paths = 0

    while len(partial_paths) != 0:
        path = partial_paths.pop()
        last_device = path[-1]
        for output in attachments[last_device]:
            if output == 'out' and end != 'out':
                continue
            if output == end:
                num_paths += 1
            elif output in path:
                continue
            else:
                partial_paths.append(path + [output])
    
    return num_paths

def solve_p1(puzzle_file):
    attachments = read_data(puzzle_file)
    return get_num_paths(attachments, 'you', 'out')

def solve_p2(puzzle_file):
    attachments = read_data(puzzle_file)
    svr_to_fft = get_num_paths_opt(attachments, 'svr', 'fft')
    svr_to_dac = get_num_paths_opt(attachments, 'svr', 'dac')
    fft_to_dac = get_num_paths_opt(attachments, 'fft', 'dac')
    dac_to_fft = get_num_paths_opt(attachments, 'dac', 'fft')
    fft_to_out = get_num_paths_opt(attachments, 'fft', 'out')
    dac_to_out = get_num_paths_opt(attachments, 'dac', 'out')

    return svr_to_fft * fft_to_dac * dac_to_out + svr_to_dac * dac_to_fft * fft_to_out

print(solve_p1('puzzle11.txt'))
print(solve_p2('puzzle11.txt'))
    