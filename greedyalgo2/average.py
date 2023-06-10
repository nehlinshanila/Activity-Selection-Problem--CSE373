import time
import random
import matplotlib.pyplot as plt

def generate_random_activities(n):
    activities = []
    for _ in range(n):
        start = random.randint(0, 999)  # Update the range to 0-999
        finish = random.randint(start + 1, 1000)
        activities.append((start, finish))
    return activities

def ActivitySelection(start, finish, n):
    activities = sorted(zip(finish, start))  # Sort activities based on finish times
    start = [activity[1] for activity in activities]
    finish = [activity[0] for activity in activities]

    print("The following activities are selected:")
    j = 0
    print(j, end=" ")
    for i in range(1, n):
        if start[i] >= finish[j]:
            print(i, end=" ")
            j = i

# Generate random activities
sizes = [10, 100, 500, 1000, 2000, 5000, 10000, 50000, 10000000]  # Number of random activities to generate
execution_times = []

for n in sizes:
    activities = generate_random_activities(n)
    start = [activity[0] for activity in activities]
    finish = [activity[1] for activity in activities]

    # Measure the execution time
    start_time = time.time()
    ActivitySelection(start, finish, n)
    end_time = time.time()

    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plotting the time complexity graph
plt.plot(sizes, execution_times, 'o-')
plt.xlabel('Number of Activities')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity of Activity Selection Algorithm')
plt.show()

