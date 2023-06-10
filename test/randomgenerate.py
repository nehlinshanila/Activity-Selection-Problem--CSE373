import random

def generate_random_activity_list(size):
    activity_prefix = "activity"

    activity_list = []

    if size < 100 :
        increment = 2
    elif size < 1000 :
        increment = 10
    elif size < 10000 :
        increment = 100
    elif size < 1000000 :
        increment = 1000
    else : 
        increment = 2000

    for i in range(1, size, 1):

        activity_name = f"{activity_prefix} {i}"
        start_time = random.randint(0, size)
        finish_time = random.randint(start_time+1, start_time+increment)
        activity = (activity_name, start_time, finish_time)
        activity_list.append(activity)

    return activity_list