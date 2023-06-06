# to test everything before the final one

data = {
  "start_time": [2 , 6 , 4 , 10 , 13 , 7],
  "finish_time": [5 , 10 , 8 , 12 , 14 , 15],
  "activity": ["Homework" , "Presentation" , "Term paper" , "Volleyball practice" , "Biology lecture" , "Hangout"]
}

selected_activity =[]
start_position = 0
# sorting the items in ascending order with respect to finish time
tem = 0
for i in range(0 , len(data['finish_time'])):
   for j in range(0 , len(data['finish_time'])):
   	 if data['finish_time'][i] < data['finish_time'][j]:
            tem = data['activity'][i], data['finish_time'][i], data['start_time'][i]
            data['activity'][i], data['finish_time'][i], data['start_time'][i] = data['activity'][j], data['finish_time'][j], data['start_time'][j]
            data['activity'][j], data['finish_time'][j], data['start_time'][j] = tem
# by default, the first activity is inserted in the list of activities to be selected.

selected_activity.append(data['activity'][start_position])
for pos in range(len(data['finish_time'])):
   if data['start_time'][pos] >= data['finish_time'][start_position]:
   	selected_activity.append(data['activity'][pos])
start_position = pos

print(f"The student can work on the following activities: {selected_activity}")
# Results
# The student can work on the following activities: ['Homework', 'Presentation', 'Volleyball practice', 'Biology lecture']