from typing import List

# API
# Return: merged list and # of inversion
def mergeAndCount(sortedArr1:List[int],sortedArr2:List[int])->tuple[List[int],int]:
    len1 = len(sortedArr1)
    len2 = len(sortedArr2)
    inversionCnt = 0
    outputArr = []

    i = 0
    j = 0
    while i<len1 and j<len2:    
        if sortedArr1[i]>sortedArr2[j] :
            outputArr.append(sortedArr2[j])
            j+=1
            inversionCnt+=1
        else:
            outputArr.append(sortedArr1[i])
            i+=1
    if i>=len1:
        [outputArr.append(remaining) for remaining in sortedArr2[j:]]
    else:
        [outputArr.append(remaining) for remaining in sortedArr1[i:]]
    
    return outputArr,inversionCnt

# print(mergeAndCount([1,3,5,11],[2,4,6,7,8,9]))