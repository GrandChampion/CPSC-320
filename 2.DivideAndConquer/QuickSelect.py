# Get the k th largest element from array

# API
# Input: k th element
# Output: k th element
def conquer(kthElement)->int:
    return kthElement

# API
# Input: 1 list and rank
# Output: k th largest element in the list
def divide(L,k)->int:
    pivot = L[0]
    Lesser=[i for i in L if i < pivot]
    Greater=[i for i in L if i>pivot]
    if len(Greater)==k-1:
        return pivot
    elif len(Greater)>k-1:
        KthElement = divide(Greater,k)
        return conquer(KthElement)
    else:
        KthElement = divide(Lesser,k-len(Greater)-1)
        return conquer(KthElement)

print(divide([2,4,6,8,1,2,5,3],3))