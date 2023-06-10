import React, { useEffect, useState } from 'react';

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
  const ActivitySelectionVisualization = () => {
    const [activityList, setActivityList] = useState([]);
    const [selectedActivities, setSelectedActivities] = useState([]);
    const [visualizationIndex, setVisualizationIndex] = useState(0);
  
    useEffect(() => {
      // Generate random activity list
      const generatedActivityList = generateRandomActivityList(10);
      setActivityList(generatedActivityList);
  
      // Perform activity selection
      const performActivitySelection = () => {
        const sortedActivities = mergeSort(generatedActivityList);
        setSelectedActivities([sortedActivities[0]]);
        let prevFinishTime = sortedActivities[0][2];
  
        // Simulate the algorithm steps with a delay
        for (let i = 1; i < sortedActivities.length; i++) {
          setTimeout(() => {
            setVisualizationIndex(i);
            if (sortedActivities[i][1] >= prevFinishTime) {
              setSelectedActivities((prevSelectedActivities) => [...prevSelectedActivities, sortedActivities[i]]);
              prevFinishTime = sortedActivities[i][2];
            }
          }, i * 1000); // Delay for visualization purposes (1 second interval)
        }
      };
  
      performActivitySelection();
    }, []);
  
    return (
      <div>
        <h2>Activity Selection Visualization</h2>
        <div>
          {activityList.map((activity, index) => (
            <div
              key={index}
              style={{
                backgroundColor: index === visualizationIndex ? 'blue' : selectedActivities.includes(activity) ? 'green' : 'gray',
                width: '50px',
                height: `${activity[2] * 2}px`,
                margin: '2px',
                display: 'inline-block',
              }}
            ></div>
          ))}
        </div>
      </div>
    );
  };
  
  const Main = () => {
    return (
      <div>
        <h1>Activity Selection</h1>
        <ActivitySelectionVisualization />
      </div>
    );
  };
  
  export default Main;