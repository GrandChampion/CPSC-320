from typing import List


def countInversion(arr:List[int])->int:
    count = 0
    inversions = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count = count+1
                inversions.append((arr[i],arr[j]))
    return count


print(countInversion([3,4,1,2]))