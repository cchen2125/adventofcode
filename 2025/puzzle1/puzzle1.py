with open("puzzle1.txt", "r") as file:
    input_data = file.read().splitlines()

dial = [i for i in range(100)]

pos = 50
zero_end_count = 0
pass_zero_count = 0

for move in input_data:
    direction = move[0]
    rotation_amount = int(move[1:])
    if direction == 'L':
        if pos - rotation_amount < 0:
            pass_zero_increment = (rotation_amount - pos) // 100 + 1
            if pos == 0:
                pass_zero_increment = pass_zero_increment - 1
            # print(pos, move, pass_zero_increment)
            pass_zero_count += pass_zero_increment
            pos = (pos - rotation_amount) % 100
        else:
            pos = (pos - rotation_amount) % 100
            if pos == 0:
                pass_zero_count += 1
    if direction == 'R':
        if pos + rotation_amount > 100:
            pass_zero_increment = (rotation_amount + pos) // 100
            #print(pos, move,pass_zero_increment)
            pass_zero_count += pass_zero_increment
            pos = (pos + rotation_amount) % 100
        else:
            pos = (pos + rotation_amount) % 100
            if pos == 0:
                pass_zero_count += 1
    if pos == 0:
        zero_end_count += 1
        #pass_zero_count += 1

print('Part 1', zero_end_count)
print('Part 2', pass_zero_count)
        

