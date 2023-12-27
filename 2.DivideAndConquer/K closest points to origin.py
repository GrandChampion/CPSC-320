import math

from typing import List

# API
# Input: 2 sorted list of points
# Output: 1 merged sorted list of points
def conquer(LeftPoints,RightPoints)->List[List[int]]:
    i=0
    j=0
    mergedSortedList = []
    while i < len(LeftPoints) and j < len(RightPoints):
        if math.sqrt(LeftPoints[i][0]**2+LeftPoints[i][1]**2)>math.sqrt(RightPoints[i][0]**2+RightPoints[i][1]**2):
            mergedSortedList.append(LeftPoints[i])
            i+=1
        else:
            mergedSortedList.append(RightPoints[j])
            j+=1
    if i >= len(LeftPoints):
        mergedSortedList.append(RightPoints[j:])
    else:
        mergedSortedList.append(LeftPoints[i:])
    return mergedSortedList

# API
# Input: 1 list
# Output: 1 Sorted list
# What it does: divide original list into small pieces until 1 element array, then combine simultanesly sorting
def divide(Points)->List[List[int]]:
    if len(Points)==1:
        return Points
    else:
        LeftSubList = Points[0:len(Points)//2]
        RightSubList = Points[len(Points)//2:]
        Left = divide(LeftSubList)
        Right = divide(RightSubList)
        Merged = conquer(Left,Right)
        return Merged


def kClosest(points: List[List[int]], k: int)->List[List[int]]:
    sortedList = divide(points)
    return sortedList[:k]
    
    

print(kClosest([[3,3],[5,-1],[-2,4]],2))