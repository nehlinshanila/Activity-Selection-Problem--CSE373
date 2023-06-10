import random
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
        if left[left_index][1] <= right[right_index][1]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def activity_selection(arr):
    n = len(arr)
    sorted_activities = merge_sort(arr)
    selected_activities = [sorted_activities[0]]
    prev_finish_time = sorted_activities[0][1]

    for i in range(1, n):
        if sorted_activities[i][0] >= prev_finish_time:
            selected_activities.append(sorted_activities[i])
            prev_finish_time = sorted_activities[i][1]

    return selected_activities

def generate_random_array(size):
    activities = []
    for _ in range(size):
        start_time = random.randint(0, 1000)
        finish_time = start_time + random.randint(1, 100)
        activities.append((start_time, finish_time))
    return activities

def write_to_file(activities, filename):
    with open(filename, 'w') as file:
        for activity in activities:
            file.write(f"Start time: {activity[0]}, Finish time: {activity[1]}\n")

def plot_graph(activities):
    start_times = [activity[0] for activity in activities]
    finish_times = [activity[1] for activity in activities]

    plt.plot(start_times, finish_times, marker='.')
    plt.xlabel('Start Time')
    plt.ylabel('Finish Time')
    plt.title('Activity Selection')
    plt.grid(True)
    plt.show()

# Main program
sizes = [100, 1000, 10000]
filename = 'activity_times.txt'

for size in sizes:
    activities = generate_random_array(size)
    selected_activities = activity_selection(activities)
    write_to_file(selected_activities, filename)
    plot_graph(selected_activities)
