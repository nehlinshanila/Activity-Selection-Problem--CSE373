// gpt did this not me
function mergeSort(arr) {
    if (arr.length <= 1) {
      return arr;
    }
  
    const mid = Math.floor(arr.length / 2);
    const leftHalf = arr.slice(0, mid);
    const rightHalf = arr.slice(mid);
  
    const leftSorted = mergeSort(leftHalf);
    const rightSorted = mergeSort(rightHalf);
  
    return merge(leftSorted, rightSorted);
  }
  
  function merge(left, right) {
    const merged = [];
    let leftIndex = 0;
    let rightIndex = 0;
  
    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex][2] <= right[rightIndex][2]) { // Comparing finish times
        merged.push(left[leftIndex]);
        leftIndex++;
      } else {
        merged.push(right[rightIndex]);
        rightIndex++;
      }
    }
  
    merged.push(...left.slice(leftIndex));
    merged.push(...right.slice(rightIndex));
  
    return merged;
  }
  
  function activitySelection(arr) {
    const sortedActivities = mergeSort(arr);
    const selectedActivities = [sortedActivities[0]];
    let prevFinishTime = sortedActivities[0][2];
  
    for (let i = 1; i < sortedActivities.length; i++) {
      const activity = sortedActivities[i];
      if (activity[1] >= prevFinishTime) {
        selectedActivities.push(activity);
        prevFinishTime = activity[2];
      }
    }
  
    return selectedActivities;
  }
  
  function generateRandomActivityList(size) {
    const activityPrefix = 'activity';
    const activityList = [];
  
    for (let i = 1; i <= size; i++) {
      const activityName = `${activityPrefix} ${i}`;
      const startTime = Math.floor(Math.random() * 101);
      const finishTime = Math.floor(Math.random() * (101 - startTime + 1)) + startTime;
      const activity = [activityName, startTime, finishTime];
      activityList.push(activity);
    }
  
    return activityList;
  }
  
  // Generate random activity list
  const activityList = generateRandomActivityList(10);
  console.log('Original Activity List:');
  activityList.forEach(activity => {
    console.log(activity);
  });
  
  // Measure execution time
  const startTime = new Date().getTime();
  const selectedActivities = activitySelection(activityList);
  const endTime = new Date().getTime();
  
  const executionTime = (endTime - startTime) / 1000;
  console.log('Execution Time:', executionTime, 'seconds');
  
  // Plot time complexity graph
  const sizes = [10, 100, 500, 1000, 2000, 5000, 10000];
  const times = [];
  
  for (let i = 0; i < sizes.length; i++) {
    const size = sizes[i];
    const activityList = generateRandomActivityList(size);
    const startTime = new Date().getTime();
    activitySelection(activityList);
    const endTime = new Date().getTime();
    const executionTime = (endTime - startTime) / 1000;
    times.push(executionTime);
  }
  
  console.log('Input Size:', sizes);
  console.log('Execution Times:', times);
  // Note: Generating the graph requires additional libraries or frameworks in JavaScript.
  // You can use charting libraries like Chart.js or Plotly.js to plot the time complexity graph.
  