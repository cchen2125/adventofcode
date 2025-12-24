import numpy as np

# Part 1
with open("puzzle1_2024.txt", "r") as file:
    input_data = file.read().splitlines()

data_array = np.array([row.split() for row in input_data]).astype(int)
left_list = data_array[:,0]
right_list = data_array[:,1]

left_list.sort()
right_list.sort()

print('Part 1 answer')
print(np.sum(abs(left_list - right_list)))

# Part 2
similarity_score = 0

for num in left_list:
    if num in right_list:
        similarity_score += num * list(right_list).count(sum)

print('Part 2 Answer')
print(similarity_score)