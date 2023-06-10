# Python Code for Activity Selection
# Function for Activity Selection
#  greedy approach to select activities.
def ActivitySelection(start, finish, n):
    print("The following activities are selected:");
    # The start list represents the start times of various activities, 
    # while the finish list represents their corresponding finish times. 
    # The n variable stores the length of the start list.
    j = 0
    # t starts by selecting the first activity (j = 0) and prints its index. 
    print(j,end=" ")
    # Then, it iterates through the remaining activities using a for loop.
    for i in range(1,n):
        # If the start time of the current activity (start[i]) is 
        # greater than or equal to the finish time of the 
        # last selected activity (finish[j]), it selects the current activity,
        #  prints its index, and updates j to the current activity's index.
        if start[i] >= finish[j]:
            print(i,end=" ")
            j = i
# Driver Code
start = [1, 3, 2, 0, 5, 8, 11]
finish = [3, 4, 5, 7, 9, 10, 12]
n = len(start)
ActivitySelection(start, finish, n)
# Output
# The following activities are selected:
# 0 1 4 6    