def activity_selection(arr):
    # sorted_activities = merge_sort(arr)
    selected_activity = arr[0]
    sorted_activities = []
    sorted_activities.append(selected_activity)

    for activity in arr:
        if activity[1] >= selected_activity[2]:
            sorted_activities.append(activity)
            selected_activity = activity

    return selected_activity