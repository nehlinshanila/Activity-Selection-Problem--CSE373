import random

def generate_random_activities(n):
    activities = []
    for _ in range(n):
        start = random.randint(0, 1000)
        finish = random.randint(start + 1, 1000)
        activities.append((start, finish))
    return activities

def ActivitySelection(start, finish, n):
    print("The following activities are selected:")
    j = 0
    print(j, end=" ")
    for i in range(1, n):
        if start[i] >= finish[j]:
            print(i, end=" ")
            j = i

# Generate random activities
n = 10  # Number of random activities to generate
activities = generate_random_activities(n)
start = [activity[0] for activity in activities]
finish = [activity[1] for activity in activities]

ActivitySelection(start, finish, n)
