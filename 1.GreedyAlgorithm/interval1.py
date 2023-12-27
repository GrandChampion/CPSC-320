# 252. Meeting room 1
# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

from typing import List


def overlapChecker(intervals: List[List[int]]) -> bool:
    if len(intervals) == 0:
        return True
    else:
        # sort by starting time of each intervals
        intervals.sort(key=lambda x: x[0])
        previousEnd = intervals[0][1]
        for interval in intervals[1:]:
            # Check if previous interval's end time and current interval's start time don't overlap
            if previousEnd <= interval[0]:
                previousEnd = interval[1]
            else:
                return False
        return True
