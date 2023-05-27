import random
import time

def generate_random_array(min_size, max_size, min_value, max_value):
    size = random.randint(min_size, max_size)  # Generate a random size within the specified range
    return [random.randint(min_value, max_value) for _ in range(size)]

min_size = 10  # Specify the minimum size of the array
max_size = 10000  # Specify the maximum size of the array
min_value = 1  # Specify the minimum value of the array
max_value = 100  # Specify the maximum value of the array

start_time = time.time()  # Start measuring the execution time
random_array = generate_random_array(min_size, max_size, min_value, max_value)
end_time = time.time()  # Stop measuring the execution time

execution_time = end_time - start_time
print(f"Execution time for generating the random array: {execution_time} seconds")
print(random_array)
