# 253. Meeting Rooms 2
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

from typing import List


def requiredRooms(intervals: List[List[int]]) -> int:
    startTime = [i[0] for i in intervals]
    startTime = sorted(startTime)

    endTime = [i[1] for i in intervals]
    endTime = sorted(endTime)

    maxRequired = 0
    currentRequired = 0

    curStartTimeIndex = 0
    curEndTimeIndex = 0

    while curStartTimeIndex < len(intervals):
        if endTime[curEndTimeIndex] > startTime[curStartTimeIndex]:
            curStartTimeIndex += 1
            currentRequired += 1
        else:
            curEndTimeIndex += 1
            currentRequired -= 1
        maxRequired = max(maxRequired, currentRequired)

    return maxRequired


print(requiredRooms([[1, 2], [1, 5], [2, 6], [3, 5], [6, 7]]))
