import random
import time
import matplotlib.pyplot as plt

def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

min_size = 10
max_size = 10000
min_value = 1
max_value = 1000
num_iterations = 10

sizes = []
execution_times = []

for size in range(min_size, max_size+1, (max_size-min_size)//num_iterations):
    sizes.append(size)
    start_time = time.time()
    random_array = generate_random_array(size, min_value, max_value)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

print(f"Array sizes: {sizes}")
print(f"Execution times: {execution_times}")

# Plotting the execution times
plt.plot(sizes, execution_times, marker='o')
plt.xlabel("Array Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time of Random Array Generation")
plt.show()
