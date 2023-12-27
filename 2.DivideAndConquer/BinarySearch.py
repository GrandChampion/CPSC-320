from typing import List

# API
# Input: number of elements before input sublist in the previous level, lengthOfSubList
# Output: index of target at that level
def conquer(elementsFront,lengthOfSubList):
    return elementsFront+lengthOfSubList

# API
# Input: 1 sorted list and a target value
# Output: index of target value inside input list, which is sorted
def divide(nums: List[int], target: int) -> int:

    if len(nums) == 1 and nums[0] == target:
            return 0
    else:
        middleIndex = len(nums)//2
        if nums[middleIndex]<target:
            SubList = divide(nums[middleIndex+1:],target)
            return conquer(len(nums[:middleIndex+1]), SubList)
        else:
            SubList = divide(nums[:middleIndex],target)
            return conquer(0,SubList)

print(divide([-1,0,3,5,9,12],9))