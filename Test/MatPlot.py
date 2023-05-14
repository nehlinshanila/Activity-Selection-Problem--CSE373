import matplotlib.pyplot as plt

# Plot the results
#           X-axis        Y-axis
plt.plot(input_sizes, execution_times, marker='o') #here the input_sizes and execution_times are the values we got from the calculations beforehand.
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Bubble Sort Time Complexity')
plt.grid(True)
plt.show()