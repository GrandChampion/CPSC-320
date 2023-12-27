from typing import List

# API
# Input: pivot of upper level, Left sublist, Right sublist
# Output: Merged list
def conquer(pivot,LeftList,RightList)->List[int]:
    return LeftList+[pivot]+RightList

# API
# Input: 1 List
# Output: Sorted list
def divide(L:List[int])->List[int]:
    if len(L) <= 1:
        return L
    else:
        pivot = L[0]
        Lesser = [element for element in L[1:] if element<pivot]
        Greater = [element for element in L[1:] if element>pivot]
        Left = divide(Lesser)
        Right = divide(Greater)
        return conquer(pivot,Left,Right)

print(divide([5,4,2,7,8,9,2,3,5,1]))
