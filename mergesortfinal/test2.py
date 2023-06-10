import random

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
activity_list = generate_random_activity_list(10)
print("Original Activity List:")
for activity in activity_list:
    print(activity)

# Perform activity selection
selected_activities = activity_selection(activity_list)

print("\nSelected Activities:")
for activity in selected_activities:
    print(activity)


#  O(n log n)