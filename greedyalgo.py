def activity_selection(start_times, end_times):
    # The activity_selection function takes two input lists: start_times and end_times, representing the start and end times of the activities, respectively.
    n = len(start_times)
    # n is assigned the length of the start_times list, which represents the number of activities.
    activities = list(zip(start_times, end_times))
    # activities is created by combining the start_times and end_times lists using the zip function. It forms a list of tuples where each tuple contains the start and end time of an activity.
    activities.sort(key=lambda x: x[1])  # Sort activities by end times
    # The activities list is sorted in ascending order based on the end times of the activities using the sort method and a lambda function as the key.
    

    selected_activities = [activities[0]]  # Select the first activity
    # selected_activities is initialized as a list containing the first activity from the sorted activities list.

    for i in range(1, n):
        if activities[i][0] >= selected_activities[-1][1]:
            # The loop starts from the second activity (i = 1) since the first activity is already selected.
            # Inside the loop, it checks if the start time of the current activity (activities[i][0]) is greater than or equal to the end time of the previously selected activity (selected_activities[-1][1]).
            selected_activities.append(activities[i])
            # If the condition is satisfied, it means the current activity is non-overlapping with the previously selected activities, so it is appended to the selected_activities list.


    return selected_activities
# The selected_activities list, containing the maximum set of non-overlapping activities, is returned from the function.
# Example usage
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
# In the example usage section, two lists, start_times and end_times, are defined to represent the start and end times of the activities.

selected_activities = activity_selection(start_times, end_times)
print(selected_activities)
# The activity_selection function is called with the start_times and end_times lists, and the resulting selected_activities list is printed.

#* {{{The overall idea of the algorithm is to sort the activities based on their 
#* end times and greedily select the activities with the earliest end times 
#* that do not overlap with each other. By doing so, the algorithm guarantees 
#* the maximum set of non-overlapping activities.}}}