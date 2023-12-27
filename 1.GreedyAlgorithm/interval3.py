# 435. Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

from typing import List


def removeOverlappingIntervals(intervals: List[List[int]]) -> int:
    removed = 0
    selectedEndTime = intervals[0][1]

    # Sanity check: sort based on start time
    sorted(intervals, key=lambda x: x[0])

    for interval in intervals[1:]:
        if interval[0] < selectedEndTime:
            # remove overlapping interval that ends late
            removed += 1
            selectedEndTime = min(selectedEndTime, interval[1])
        else:
            # nothing to remove
            selectedEndTime = interval[1]
    return removed


print(removeOverlappingIntervals(
    [[1, 2], [2, 3], [3, 4], [1, 3]]))
