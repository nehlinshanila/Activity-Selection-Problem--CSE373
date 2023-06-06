def activity_selection(start, finish):
    n = len(start)

    # Sort activities by their finish times
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected_activities = [activities[0]]  # Select the first activity
    prev_finish_time = activities[0][1]

    # Iterate through the sorted activities
    for i in range(1, n):
        current_activity = activities[i]
        current_start_time = current_activity[0]

        # If the current activity's start time is after the previous activity's finish time, select it
        if current_start_time >= prev_finish_time:
            selected_activities.append(current_activity)
            prev_finish_time = current_activity[1]

    return selected_activities


# Example usage
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]

selected = activity_selection(start_times, finish_times)

print("Selected activities:")
for activity in selected:
    print(f"Start time: {activity[0]}, Finish time: {activity[1]}")
