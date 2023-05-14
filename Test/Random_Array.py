import random

Random_start = 1
Random_end = 101

Size_of_Array = 10
# This will generate an array of 10 random unique integers between 1 and 100
my_array = random.sample(range(Random_start, Random_end), Size_of_Array)

print(my_array)


# i will update thhe Random_start, Random_end and Size_of_Array 
# with every iteration. This will generate a random number between
# the start and end and keep pushing them into the array for the sorting
# algorithm for sorting over time.