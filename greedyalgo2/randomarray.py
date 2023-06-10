# input from user. the input will be 'n'. 'n' is total number of randomly generated number of integers in an array. in python

import random

n = int(input("Enter the total number of integers: "))
# The input function is used to prompt the user for the total number of integers (n)
array = [random.randint(1, 100) for _ in range(n)]
print("Randomly generated array:", array)
