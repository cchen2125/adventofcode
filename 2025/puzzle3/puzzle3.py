with open("puzzle3.txt", "r") as file:
    banks = file.read().splitlines()

def solve_p1(banks):

    total_joltage = 0

    for bank in banks:
        batteries = [int(digit) for digit in bank]
        sorted_batteries = sorted(batteries[:-1])
        #print(batteries, sorted_batteries)
        max_battery = sorted_batteries[-1]
        max_index = batteries.index(max_battery)

        max_second_digit = 0
        for i in range(max_index+1, len(batteries)):
            if batteries[i] > max_second_digit:
                max_second_digit = batteries[i]

        #print(f'{max_battery}{max_second_digit}')
        total_joltage += int(f'{max_battery}{max_second_digit}')
    
    return total_joltage

def solve_p2(banks):
    total_joltage = 0

    bank_size = len(banks[0])
    num_batteries = 12

    for bank in banks:
        batteries = [int(digit) for digit in bank]
        sorted_batteries = sorted(batteries[:-1*(num_batteries - 1)])
        max_battery = sorted_batteries[-1]

        joltage = [max_battery]
        last_battery_index = batteries.index(max_battery)

        for batteries_left in range(num_batteries, 1, -1):
            max = 1
            
            for j in range(last_battery_index+1, bank_size-batteries_left+2):
                if batteries[j] > max:
                    max = batteries[j]
                    last_battery_index = j
            joltage.append(max)
        
        total_joltage += int(''.join(map(str, joltage)))

    return total_joltage

print('Part 1', solve_p1(banks))
print('Part 2', solve_p2(banks))