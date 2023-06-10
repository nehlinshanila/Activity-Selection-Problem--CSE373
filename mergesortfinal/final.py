import random
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][2] <= right[right_index][2]:  # Comparing finish times
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def activity_selection(arr):
    sorted_activities = merge_sort(arr)
    selected_activities = [sorted_activities[0]]
    prev_finish_time = sorted_activities[0][2]

    for activity in sorted_activities[1:]:
        if activity[1] >= prev_finish_time:
            selected_activities.append(activity)
            prev_finish_time = activity[2]

    return selected_activities

def generate_random_activity_list(size):
    activity_prefix = "activity"
    activity_list = []

    for i in range(1, size+1):
        activity_name = f"{activity_prefix} {i}"
        start_time = random.randint(0, 100)
        finish_time = random.randint(start_time, start_time+100)
        activity = (activity_name, start_time, finish_time)
        activity_list.append(activity)

    return activity_list

# Generate random activity list
activity_list = generate_random_activity_list(10000)

# Save original activity list to a file
with open('original_activity_list.txt', 'w') as file:
    file.write("Original Activity List (Unsorted):\n")
    for activity in activity_list:
        file.write(str(activity) + '\n')

# Measure execution time
start_time = time.time()

# Merge sort
sorted_activities = merge_sort(activity_list)

# Activity selection
selected_activities = activity_selection(sorted_activities)

end_time = time.time()

execution_time = end_time - start_time

# Save sorted activity list to a file
with open('sorted_activity_list.txt', 'w') as file:
    file.write("Sorted Activity List:\n")
    for activity in sorted_activities:
        file.write(str(activity) + '\n')

print("Total Execution Time:", execution_time, "seconds")

# Plot time complexity graph
min_size = 10
max_size = 100000
step = 100

sizes = list(range(min_size, max_size + 1, step))
times = []

for size in sizes:
    activity_list = generate_random_activity_list(size)
    start_time = time.time()
    # Merge sort
    sorted_activities = merge_sort(activity_list)
    # Activity selection
    selected_activities = activity_selection(sorted_activities)

    end_time = time.time()
    execution_time = end_time - start_time
    times.append(execution_time)

plt.plot(sizes, times, marker='.')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity Graph')
plt.grid(True)
plt.show()
