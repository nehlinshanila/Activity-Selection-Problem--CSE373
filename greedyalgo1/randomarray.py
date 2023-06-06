import random

def generate_random_array(min_size, max_size, min_value, max_value):
    size = random.randint(min_size, max_size)  # Generate a random size within the specified range
    return [random.randint(min_value, max_value) for _ in range(size)]

min_size = 10  # Specify the minimum size of the array
max_size = 10000  # Specify the maximum size of the array
min_value = 1  # Specify the minimum value of the array
max_value = 100  # Specify the maximum value of the array

random_array = generate_random_array(min_size, max_size, min_value, max_value)
print(random_array)
