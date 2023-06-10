import React, { useEffect, useState } from 'react';

function mergeSort(arr) {
  if (arr.length <= 1) {
    return Promise.resolve(arr);
  }

  const mid = Math.floor(arr.length / 2);
  const leftHalf = arr.slice(0, mid);
  const rightHalf = arr.slice(mid);

  return Promise.all([mergeSort(leftHalf), mergeSort(rightHalf)]).then(([leftSorted, rightSorted]) => {
    return merge(leftSorted, rightSorted);
  });
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

  return merged.concat(left.slice(leftIndex), right.slice(rightIndex));
}

function activitySelection(arr) {
  return mergeSort(arr).then(sortedActivities => {
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
  });
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
  const [activityPositions, setActivityPositions] = useState([]);

  useEffect(() => {
    // Generate random activity list
    const generatedActivityList = generateRandomActivityList(10);
    setActivityList(generatedActivityList);

    // Perform activity selection with animation
    const performActivitySelection = async (activities) => {
      const sortedActivities = await activitySelection(activities);
      setSelectedActivities([]);
      setVisualizationIndex(0);
      setActivityPositions(activities.map((_, index) => index * 60));

      const animateSorting = async () => {
        for (let i = 0; i < sortedActivities.length; i++) {
          await new Promise(resolve => setTimeout(resolve, 1000)); // Delay for visualization purposes (1 second interval)

          setVisualizationIndex(i);
          setSelectedActivities(sortedActivities.slice(0, i + 1));

          const sortedIndex = activities.findIndex(activity => activity[0] === sortedActivities[i][0]);
          setActivityPositions(prevPositions => {
            const newPositions = [...prevPositions];
            newPositions[sortedIndex] = i * 60;
            return newPositions;
          });
        }
      };

      animateSorting();
    };

    performActivitySelection(generatedActivityList);
  }, []);

  return (
    <div>
      <h2>Activity Selection Visualization</h2>
      <div style={{ display: 'flex' }}>
        {activityList.map((activity, index) => (
          <div
            key={index}
            style={{
              backgroundColor: selectedActivities.includes(activity) ? 'green' : 'gray',
              width: '50px',
              height: `${activity[2] * 2}px`,
              margin: '2px',
              display: 'inline-block',
              transform: `translateX(${activityPositions[index]}px)`,
              transition: 'transform 1s ease-in-out',
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
