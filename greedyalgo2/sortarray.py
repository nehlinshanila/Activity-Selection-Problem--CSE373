import random
import matplotlib.pyplot as plt

def generate_activities(n, min_start_time, max_start_time, min_finish_time, max_finish_time):
    activities = [{'id': i + 1,
                   'start_time': random.randint(min_start_time, max_start_time),
                   'finish_time': random.randint(min_finish_time, max_finish_time)}
                  for i in range(n)]
    return activities

def select_activities(activities):
    sorted_activities = sorted(activities, key=lambda x: x['finish_time'])
    selected_activities = [sorted_activities[0]]  # Select the first activity
    last_finish_time = sorted_activities[0]['finish_time']
    
    for activity in sorted_activities[1:]:
        if activity['start_time'] >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = activity['finish_time']
    
    return selected_activities

# Generate random activities
activities = generate_activities(1000, 1, 100, 101, 200)

# Sort the activities
sorted_activities = select_activities(activities)

# Plot the start and finish times of all activities
start_times = [activity['start_time'] for activity in activities]
finish_times = [activity['finish_time'] for activity in activities]

plt.figure(figsize=(10, 6))
plt.scatter(start_times, range(1, len(start_times) + 1), color='blue', label='Start Time')
plt.scatter(finish_times, range(1, len(finish_times) + 1), color='red', label='Finish Time')
plt.xlabel('Time')
plt.ylabel('Activity')
plt.title('Activities')
plt.legend()
plt.show()
