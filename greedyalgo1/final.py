import random
import timeit
import matplotlib.pyplot as plt

def generate_random_activities(num_activities, min_start_time, max_start_time, min_duration, max_duration):
    activities = []
    # activities = []: This creates an empty list to store the generated activities.
    used_times = set()  # Keep track of used time intervals
    # used_times = set(): This creates an empty set to keep track of used time intervals. A set is used to ensure uniqueness of time intervals.

    for _ in range(num_activities):
        # for _ in range(num_activities):: This starts a loop that will iterate num_activities times. The underscore _ is used as a throwaway variable since we don't need its value.
        while True:
            # while True:: This starts an infinite loop that will continue until a unique time interval is generated.
            start_time = random.randint(min_start_time, max_start_time)
            # start_time = random.randint(min_start_time, max_start_time): This generates a random integer within the specified range as the start time for an activity.
            duration = random.uniform(min_duration, max_duration)
            # duration = random.uniform(min_duration, max_duration): This generates a random floating-point number within the specified range as the duration of an activity.
            end_time = start_time + duration
            # end_time = start_time + duration: This calculates the end time of the activity by adding the start time and duration.

            time_interval = (start_time, end_time)
            # time_interval = (start_time, end_time): This creates a tuple representing the time interval of the activity.
            if time_interval not in used_times:
                # if time_interval not in used_times:: This checks if the generated time interval is not already in the set of used times.
                used_times.add(time_interval)
                # used_times.add(time_interval): If the time interval is unique, it is added to the set of used times.
                activities.append((start_time, end_time))
                # activities.append((start_time, end_time)): The start and end time of the activity are appended as a tuple to the activities list.
                break
            # break: This breaks out of the inner loop, allowing the next activity to be generated.

    return activities
# return activities: Finally, the list of generated activities is returned.

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort activities by end times\
    # activities.sort(key=lambda x: x[1]): This sorts the list of activities based on the end times of each activity. The key parameter specifies that the sorting should be based on the second element of each tuple (the end time).

    selected_activities = []
    # selected_activities = []: This creates an empty list to store the selected activities.
    last_end_time = float('-inf')
    # last_end_time = float('-inf'): This initializes the variable last_end_time with a value of negative infinity. It represents the end time of the previously selected activity.

    for activity in activities:
        # for activity in activities:: This iterates over each activity in the sorted list of activities.
        start_time, end_time = activity
        # start_time, end_time = activity: This unpacks the tuple representing the current activity into separate variables start_time and end_time.
        if start_time >= last_end_time:
            # if start_time >= last_end_time:: This checks if the start time of the current activity is greater than or equal to the end time of the previously selected activity. If it is, it means that the current activity can be selected without overlapping with the previous one.
            selected_activities.append(activity)
            # selected_activities.append(activity): If the current activity satisfies the condition, it is appended to the list of selected activities.
            last_end_time = end_time
            # last_end_time = end_time: The end time of the current activity is assigned to last_end_time, updating it for the next iteration.

    return selected_activities
# return selected_activities: Finally, the list of selected activities is returned.

# Lists to store the data for plotting
num_activities = []
execution_times = []
# These two empty lists will be used to store the number of activities and their corresponding execution times for different input sizes.

# Generate random activities once for all input sizes
max_num_activities = 1000
activities_set = generate_random_activities(max_num_activities, 0, 100, 1, 10)
# Here, max_num_activities is set to 1000, representing the maximum number of activities to consider. The generate_random_activities function is called to generate a set of random activities with the specified parameters: 
# num_activities (maximum number of activities), min_start_time, max_start_time, min_duration, and max_duration. The resulting activities are stored in the activities_set variable.

# Generate random activities and measure execution time
for n in range(10, 1000, 10):
    random_activities = activities_set[:n]  # Use a subset of activities for each input size
    # This loop iterates over a range of values from 100 to 1000 (inclusive) with a step size of 100. For each value n, a subset of activities is extracted from activities_set using slicing (activities_set[:n]). This subset represents the activities for the current input size. 

    # Perform multiple iterations to get an average execution time
    num_iterations = 10
    execution_time = timeit.timeit(lambda: activity_selection(random_activities), number=num_iterations)
    # The variable num_iterations is set to 10, representing the number of iterations to be performed to measure the execution time. The timeit.timeit function is used to measure the execution time of the activity_selection function. 
    # The lambda function lambda: activity_selection(random_activities) creates a callable object that executes the activity_selection function with the random_activities as its argument. 
    # The number parameter specifies the number of times to execute the callable.

    average_execution_time = execution_time / num_iterations
    # The execution_time is divided by num_iterations to calculate the average execution time.

    # Append data to the lists
    num_activities.append(n)
    execution_times.append(average_execution_time)
    # The current input size (n) and the average execution time are appended to the num_activities and execution_times lists, respectively.

# Plot the graph
plt.plot(num_activities, execution_times, marker='.')
plt.xlabel('Number of Activities')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Activity Selection Algorithm')
plt.show()
# The plt.plot function is used to plot the graph with num_activities on the x-axis and execution_times on the y-axis. The plt.xlabel, plt.ylabel, and plt.title functions are used to set the labels for the x-axis, y-axis, and the title of the graph, respectively.

# Save the graph as a PNG image
# plt.savefig('time_complexity_graph.png')
# The plt.savefig function is used to save the graph as a PNG image file named "time_complexity_graph.png". It takes the file name as an argument.

# Display a message after saving the image
# print("Time complexity graph saved as 'time_complexity_graph.png'.")


# {{{This code generates random activities with specified
#  start times and durations, measures the execution time 
# of an activity selection algorithm for different input 
# sizes, plots a graph showing the relationship between 
# the number of activities and their execution times, and
#  saves the graph as a PNG image.}}}