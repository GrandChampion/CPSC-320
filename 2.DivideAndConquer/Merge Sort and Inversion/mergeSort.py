from typing import List

# API
# Input: 2 sorted arrays
# returns: Combined list of sorted array
def conquer(LeftArray,RightArray)->List[int]:
    i = 0
    j = 0
    CombinedArray = []

    while i <len(LeftArray) and j<len(RightArray):
        if LeftArray[i]>RightArray[j]:
            CombinedArray.append(RightArray[j])
            j+=1
        else:
            CombinedArray.append(LeftArray[i])
            i+=1
    if i == len(LeftArray):
        [CombinedArray.append(item) for item in RightArray[j:]] 
    elif j == len(RightArray):
        [CombinedArray.append(item) for item in LeftArray[i:]]

    return CombinedArray

# API
# Input: 
# Output: 
def divide(L:List[int])->List[int]:
    if len(L) == 1:
        return L
    else:
        # Divide
        leftSubArray = L[:len(L)//2]
        rightSubArray = L[len(L)//2:]
        Left = divide(leftSubArray)
        Right = divide(rightSubArray)
        
        # Conquer
        return conquer(Left,Right)

x= divide([8,4,3,2,6,7,8,1])
print(x)