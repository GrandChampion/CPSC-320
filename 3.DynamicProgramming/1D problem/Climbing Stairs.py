# Memoization (Top->Bottom: using while loop or recursion)
def memoClimbStairs(n):
    solution = [-1 for i in range(n + 1)]
    return memoClimbStairsHelper(solution, n)


def memoClimbStairsHelper(sol, i):
    if sol[i] != -1:
        return sol[i]
    elif i < 0:
        return 0
    elif i == 0:
        sol[i] = 1
    else:
        sol[i] = memoClimbStairsHelper(sol, i - 1) + memoClimbStairsHelper(sol, i - 2)
    return sol[i]


# print(memoClimbStairs(2))

##############################################################################################################################
# Dynamic Programming (Bottom->Up: using for loop)
def dynamicClimbStairs(n):
    solution = [-1 for i in range(n + 1)]
    for i in range(1, n + 1):
        solution[i] = dynamicClimbStairsHelper(
            solution, i - 1) + dynamicClimbStairsHelper(solution, i - 2)
    return solution[n]


def dynamicClimbStairsHelper(sol, k):
    if k < 0:
        return 0
    elif k == 0:
        return 1
    else:
        return sol[k]

# print(dynamicClimbStairs(3))
