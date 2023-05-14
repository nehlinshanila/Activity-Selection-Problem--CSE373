execution_times = []

with open('execution_times.txt', 'r') as file:
    for line in file:
        time = float(line.strip())
        execution_times.append(time)

print(execution_times)
