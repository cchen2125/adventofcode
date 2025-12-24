with open("puzzle2_2024.txt", "r") as file:
    input_data = file.read().splitlines()

reports = [list(map(int, report.split())) for report in input_data]

def check_safety(report):
    if report[1] > report[0]:
        direction = 'increasing'
    elif report[1] < report[0]:
        direction = 'decreasing'
    else:
        return False
    
    for i in range(1, len(report)):
        if report[i] == report[i-1] or abs(report[i] - report[i-1]) > 3:
            return False
        
        if direction == 'increasing' and report[i] < report[i-1]:
            return False
        
        if direction == 'decreasing' and report[i] > report[i-1]:
            return False
    
    return True

def num_safe_reports(reports):
    num_safe = 0

    for report in reports:
        if check_safety(report):
            num_safe += 1
    
    return num_safe

def check_problem_damp_safe(report):
    if check_safety(report):
        return True

    for i in range(len(report)):
        removed_val = report.pop(i)
        if check_safety(report):
            return True
        
        report.insert(i, removed_val)

    return False
        

def num_problem_damp_safe(reports):
    num_safe = 0

    for report in reports:
        if check_problem_damp_safe(report):
            num_safe+=1
    
    return num_safe


print("Part 1 Answer")
print(num_safe_reports(reports))

print("Part 2 Answer")
print(num_problem_damp_safe(reports))