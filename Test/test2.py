import random
import time
import matplotlib.pyplot as plt

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
array_string = ''

def measure_time(size_of_array):
    array = [random.randint(1, size_of_array) for _ in range(size_of_array)]
    
    with open('array.txt', 'a') as file: #opening the file in append mode
        file.seek(0, 2) #move the file pointer to the end 
        file.write(f'size of {size_of_array} : {array} \n\n') #writing or appending to the last pointer of the file
    # array_string += str(arr)
    # print(f'size of {n}:{arr} \n\n')
    # array_string += str(f'size of {n}:{array} \n\n')
    
    start_time = time.time()
    heap_sort(array)
    end_time = time.time()

    return end_time - start_time

# Define the input sizes
# input_sizes = [100, 500, 1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000]
input_size_start = 10
input_size_end = 10000
# input_sizes = [100, 500, 1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000]

input_sizes = []

while input_size_start <= input_size_end:
    input_sizes.append(input_size_start)
    
    if input_size_start < 100:
        input_size_start += 10
    elif input_size_start < 1000:
        input_size_start += 100
    elif input_size_start < 10000:
        input_size_start += 1000
    else:
        input_size_start += 10000
    
    

# Measure the execution time for each input size
execution_times = []
start_time_total = time.time()
for size in input_sizes:
    execution_time = measure_time(size)
    execution_times.append(execution_time)

end_time_total = time.time()
# Write execution_times to a text file
with open('execution_times.txt', 'w') as file:
    for time, sizes in zip(execution_times, input_sizes):
        file.write(str(f'{sizes} = {time:.16f}') + '\n')


total_execution_time = end_time_total - start_time_total


# Plot the results
plt.plot(input_sizes, execution_times, marker='.')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title(f'Heap Sort Time Complexity: \n total execution time {total_execution_time:.2f}')
plt.grid(True)
plt.show()
