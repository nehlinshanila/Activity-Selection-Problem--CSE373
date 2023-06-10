import random
import matplotlib.pyplot as plt

def generate_random_activities(num_activities):
    activities = []
    for _ in range(num_activities):
        start = random.randint(0, 1000)
        finish = random.randint(start + 1, start + 1000)  # Update the upper limit for finish time
        activities.append((start, finish))
    return activities

def plot_activity_selection(start, finish):
    activities = sorted(zip(finish, start))
    
    # Create an empty plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Add nodes for activities
    for i, activity in enumerate(activities):
        ax.scatter(i, 0, c='lightblue', s=100)
        ax.annotate(f"Start: {activity[1]}\nFinish: {activity[0]}", (i, 0), xytext=(0, 10),
                    textcoords='offset points', ha='center')
    
    # Add edges for overlapping activities
    for i in range(len(activities) - 1):
        for j in range(i + 1, len(activities)):
            if activities[j][1] < activities[i][0]:
                ax.plot([i, j], [0, 0], 'k-')
    
    # Set plot title and remove axes
    ax.set_title("Activity Selection")
    ax.axis('off')
    
    # Adjust plot margins
    plt.subplots_adjust(top=0.8, bottom=0.2)
    
    # Display the plot
    plt.show()

# Example usage with 10,000 random activities
num_activities = 1000
activities = generate_random_activities(num_activities)

start_times = [activity[0] for activity in activities]
finish_times = [activity[1] for activity in activities]

plot_activity_selection(start_times, finish_times)
