import random
import time
import matplotlib.pyplot as plt

def generate_random_activities(num_activities, min_start_time, max_start_time, min_duration, max_duration):
    activities = []
    used_times = set()  # Keep track of used time intervals

    for _ in range(num_activities):
        while True:
            start_time = random.randint(min_start_time, max_start_time)
            duration = random.uniform(min_duration, max_duration)
            end_time = start_time + duration

            time_interval = (start_time, end_time)
            if time_interval not in used_times:
                used_times.add(time_interval)
                activities.append((start_time, end_time))
                break

    return activities

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort activities by end times

    selected_activities = []
    last_end_time = float('-inf')

    for activity in activities:
        start_time, end_time = activity
        if start_time >= last_end_time:
            selected_activities.append(activity)
            last_end_time = end_time

    return selected_activities

# Generate random activities
num_activities = 1000
min_start_time = 0
max_start_time = 100
min_duration = 1
max_duration = 10

# Lists to store input sizes and corresponding execution times
input_sizes = []
execution_times = []

# Vary the input size and measure the execution time
for size in range(100, num_activities + 1, 100):
    # Generate random activities
    random_activities = generate_random_activities(size, min_start_time, max_start_time, min_duration, max_duration)

    # Measure execution time
    start_time = time.time()
    selected_activities = activity_selection(random_activities)
    end_time = time.time()
    execution_time = end_time - start_time

    # Store input size and execution time
    input_sizes.append(size)
    execution_times.append(execution_time)

# Plotting the graph
plt.plot(input_sizes, execution_times)
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity of Activity Selection Algorithm')
plt.show()