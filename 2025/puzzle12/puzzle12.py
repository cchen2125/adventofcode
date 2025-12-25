puzzle_file = 'puzzle12_example.txt'

with open(puzzle_file, 'r') as file:
    input_data = file.read().split('\n\n')

    # presents are a dictionary where the key is the present id and the values are the present shape as a list of lists
    presents = {
        int(item.split('\n')[0].strip(':')): 
        [[1 if c=='#' else 0 for c in line] for line in item.split('\n')[1:]] for item in input_data[:-1]
    }

    # trees are a list where each item is a tuple where the first item is a tuple of the tree dimension and the second item is a list of numbers of each present
    trees = [
        (tuple(map(int, item.split(' ')[0].strip(':').split('x'))), 
         list(map(int, item.split(' ')[1:]))) 
         for item in input_data[-1].split('\n')
    ]

num_fit = 0

for tree in trees:
    (w, h), needed_presents = tree
    area = w * h

    total_spots_needed = 0
    for i in range(len(needed_presents)):
        present = presents[i]
        occupied_spots = sum([sum(line) for line in present])
        total_spots_needed += needed_presents[i] * occupied_spots
    if total_spots_needed <= area:
        num_fit += 1
    print(total_spots_needed, area)

print(num_fit)
