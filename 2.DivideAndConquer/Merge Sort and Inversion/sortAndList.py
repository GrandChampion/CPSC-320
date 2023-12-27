from typing import List
from mergeAndCount import mergeAndCount

# API
# Return: sort input array and count inversions
def sortAndCount(inputList:List[int])->tuple[List[int],int]:
    if len(inputList) == 1:
        return (inputList, 1)
    else:
        L = inputList[:len(inputList)//2]
        R = inputList[len(inputList)//2:]
        (sortedL,inversionL) = sortAndCount(L)
        (sortedR,inversionR) = sortAndCount(R)
        (mergedList, inversionWhileMergingLR) = mergeAndCount(sortedL,sortedR)

        totalInversion = inversionL+inversionR+inversionWhileMergingLR
        return (mergedList,totalInversion)


# print(sortAndCount([8,4,3,2,6,7,8,1]))