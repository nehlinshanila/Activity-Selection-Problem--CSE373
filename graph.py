import random
import time
import matplotlib.pyplot as plt

def generate_random_array(min_size, max_size, min_value, max_value):
    size = random.randint(min_size, max_size)
    return [random.randint(min_value, max_value) for _ in range(size)]

min_size = 10
max_size = 10000
min_value = 1
max_value = 100
num_iterations = 10

execution_times = []

for _ in range(num_iterations):
    start_time = time.time()
    random_array = generate_random_array(min_size, max_size, min_value, max_value)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

print(f"Execution times: {execution_times}")

# Plotting the execution times
x_values = list(range(1, num_iterations + 1))
plt.plot(x_values, execution_times, marker='o')
plt.xlabel("Iteration")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time of Random Array Generation")
plt.show()
