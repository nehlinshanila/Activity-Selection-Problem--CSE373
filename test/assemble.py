import mergesort_modified as msm
import greedyapproach as gra 
import randomgenerate as rand

import time
import matplotlib.pyplot as plt


def measure_time(size_of_array):
    list = rand.generate_random_activity_list(size_of_array)
    
    with open('average_case_list.txt', 'a' ) as file:
        file.seek(0,2)
        file.write(f'size of list: {size_of_array} : {list} \n\n') 

    sort_start_time = time.time()
    sorted_list = msm.merge_sort(list)
    sort_end_time = time.time()

    execution_time_sort = sort_end_time - sort_start_time

    final_start_time = time.time()
    final_list = gra.activity_selection(sorted_list)
    final_end_time = time.time()

    execution_time_final = final_end_time - final_start_time

    with open('greedy_approach_list.txt', 'a') as file:
        file.seek(0,2)
        file.write(f'size of list: {size_of_array} : {final_list}')

    return(execution_time_sort, execution_time_final)


input_size_start = 10
input_size_end = 100000
# dont go above this= disaster timing

input_sizes = []
while input_size_start <= input_size_end:
    input_sizes.append(input_size_start)
    if input_size_start < 100:
        input_size_start += 10
    elif input_size_start < 1000:
        input_size_start += 100
    # elif input_size_start < 10000:
    #     input_size_start += 1000
    elif input_size_start < 1000000:
        input_size_start += 10000
    else:
        input_size_start += 10000


execution_times_sort =[]
execution_times_final = []


start_time_total = time.time() # this is the first time for the total execution
for size in input_sizes:
    sort_execution_time, final_execution_time = measure_time(size)
    execution_times_final.append(final_execution_time)
    execution_times_sort.append(sort_execution_time)

end_time_total = time.time() # this is the end time of the total execution
with open("execution_final_time.txt", "w") as file:
    for time, sizes in zip(execution_times_final, input_sizes):
        file.write(f'execution_final_time : {time}, size = {sizes}')

with open("execution_sort_time.txt", "w") as file:
    for time, sizes in zip(execution_times_sort, input_sizes):
        file.write(f'execution_sort_time : {time}, size = {sizes}')

total_execution_time = end_time_total - start_time_total
# plotting
plt.plot(input_sizes, execution_times_final, marker='.')
plt.xlabel("input_size")
plt.ylabel("execution_time")
plt.title(f'greedy_approach_time_complexity: {total_execution_time}')
plt.grid(True)

plt.show()

