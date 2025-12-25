with open('puzzle4.txt', 'r') as file:
    input_data = file.read().splitlines()
    rolls_grid = [[c for c in row] for row in input_data]

def find_roll_count(grid):
    roll_count = 0

    height = len(grid)
    width = len(grid[0])

    new_grid = [['.']* width for i in range(height)]

    for i in range(height):
        for j in range(width):
            if grid[i][j] == '@':
                new_grid[i][j] = '@'
                num_adjacent = 0
                adjacent_coords = [(-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1), (1, 0), (0, 1)]

                for k,l in adjacent_coords:
                    if 0 <= i+k < height and 0 <= j+l < width:
                        if grid[i+k][j+l] == '@':
                            num_adjacent += 1

                #print(i, j, num_adjacent)

                if num_adjacent < 4:
                    #print(i,j)
                    roll_count += 1
                    new_grid[i][j] = '.'
    
    return roll_count, new_grid

print('Part 1', find_roll_count(rolls_grid)[0])

def solve_part_2(rolls_grid):
    roll_count, new_grid = find_roll_count(rolls_grid)

    if roll_count == 0:
        return 0
    
    return roll_count + solve_part_2(new_grid)

#roll_count, new_grid = find_roll_count(rolls_grid)
print('Part 2', solve_part_2(rolls_grid))




