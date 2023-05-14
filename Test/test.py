import time
import random
import matplotlib.pyplot as plt


def bubble_sort(array):
    array_length = len(array)
    for i in range(array_length - 1):
        for j in range(array_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

Random_start = 1
Random_end = 10

Size_of_Array = Random_end              
                
def measure_time(Size_of_array):
    array = random.sample(range(Random_start, Random_end), Size_of_Array)
    start = time.time()
    
    end = time.time()
    bubble_sort(array)
    total_runtime = end - start
    return total_runtime



