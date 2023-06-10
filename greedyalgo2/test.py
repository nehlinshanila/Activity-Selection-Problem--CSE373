import random
import time
import matplotlib.pyplot as plt

def ActivitySelection(start, finish, n):
    print("The following activities are selected:");

    j = 0
    print(j,end=" ")
    for i in range(1,n):

        if start[i] >= finish[j]:
            print(i,end=" ")
            j = i

# n = int(input("Enter the total number of integers: "))
# input_sizes = [10, 100, 1000, 10000]  # Example input sizes
input_sizes = [10, 100]  # Example input sizes

execution_times = []
# start = [random.randint(1, 100) for _ in range(n)]
# finish = [start[i] + random.randint(1, 100) for i in range(n)]
# n = len(start)
# ActivitySelection(start, finish, n)
for n in input_sizes:
    start = [random.randint(1, 100) for _ in range(n)]
    finish = [start[i] + random.randint(1, 100) for i in range(n)]

    start_time = time.time()
    ActivitySelection(start, finish, n)
    end_time = time.time()

    execution_time = end_time - start_time
    execution_times.append(execution_time)

print("Randomly generated start times of activity:", start)
print("Randomly generated start times of activity:", finish)

def arrange_activities(start, finish):
    activities = [(i, start[i], finish[i]) for i in range(len(start))]
    activities.sort(key=lambda x: x[2])
    arranged_activities = [activity[0] for activity in activities]

    return arranged_activities


arranged = arrange_activities(start, finish)
print("Arranged activities:", arranged)


plt.plot(input_sizes, execution_times, marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (s)')
plt.title('Time Complexity of Activity Selection')
plt.show()
