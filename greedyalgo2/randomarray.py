import random

activities = []

def generate_activities(n, min_start_time, max_start_time, min_finish_time, max_finish_time):
    for _ in range(n):
        start_time = random.randint(min_start_time, max_start_time)
        finish_time = random.randint(min_finish_time, max_finish_time)
        activity = {'id': len(activities) + 1, 'start_time': start_time, 'finish_time': finish_time}
        activities.append(activity)

def add_activity(start_time, finish_time):
    activity = {'id': len(activities) + 1, 'start_time': start_time, 'finish_time': finish_time}
    activities.append(activity)

def print_activities():
    print("Activities:")
    for activity in activities:
        print(f"ID: {activity['id']}, Start Time: {activity['start_time']}, Finish Time: {activity['finish_time']}")
    print()

# Generate initial activities with random start and finish times
generate_activities(1000, 1, 100, 101, 200)

while True:
    print("Options:")
    print("1. Add new activity")
    print("2. Print activities")
    print("3. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        start_time = int(input("Enter the start time of the new activity: "))
        finish_time = int(input("Enter the finish time of the new activity: "))
        add_activity(start_time, finish_time)
        print("Activity added successfully.")

    elif option == 2:
        print_activities()

    elif option == 3:
        break

    else:
        print("Invalid option. Please try again.")
    print()

print("Program exited.")
