# Memoization Coin Change (Top->Bottom: using while loop or recursion)
import numpy as np


# 1D memoization은 helper 함수가 필요하다.
# memo 함수에서는 1D list를 선언하고, 함수를 부른다.


def MemoCoinChange(n):
    solution = [-1 for i in range(n + 1)]
    return MemoCoinChangeHelper(solution, n)


# API
# Input: 1D 리스트, 돈
# Output: n을 만들기 위한 최소의 동전개수
def MemoCoinChangeHelper(sol, n):
    if n < 0:
        return np.inf
    elif n == 0:
        return 0
    elif sol[n] != -1:  # 이 순서를 꼭 지켜야한다. 선언되지 않은 리스트 부분은 접근이 불가능 하다.
        return sol[n]
    else:
        sol[n] = min(MemoCoinChangeHelper(
            sol, n - 25) + 1, MemoCoinChangeHelper(sol, n - 10) + 1, MemoCoinChangeHelper(sol, n - 1) + 1)
    return sol[n]


##############################################################################################################################
# Dynamic Coin Change (Bottom->Up: using for loop)
# 1D 다이나믹 프로그래밍은 helper가 필요하다.

def dynamicCoinChange(n):
    solution = [-1 for i in range(n + 1)]
    for i in range(1, n + 1):
        solution[i] = min(dynamicCoinChangeHelper(solution, i - 25) + 1, dynamicCoinChangeHelper(
            solution, i - 10) + 1, dynamicCoinChangeHelper(solution, i - 1) + 1)
    return solution[n]


# API


def dynamicCoinChangeHelper(sol, k):
    if k < 0:
        return np.inf
    elif k == 0:
        return 0
    else:
        return sol[k]


# print(dynamicCoinChange(100))


##############################################################################################################################
# Extract coin types
solution1 = [-1 for i in range(28)]
MemoCoinChangeHelper(solution1, 27)
print(solution1)


def extractChange(solution, n):
    twentyFive = 0
    ten = 0
    one = 0
    while n > 0:
        if solution[n] == solution[n - 1] + 1 or n == 1:
            n -= 1
            one += 1
        elif solution[n] == solution[n - 10] + 1:
            n -= 10
            ten += 1
        else:
            n -= 25
            twentyFive += 1
    return (one, ten, twentyFive)


print(extractChange(solution1, 27))
