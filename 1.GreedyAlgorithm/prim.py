from typing import List
thegraph = [[0, 2, 0, 6],
            [2, 0, 3, 8],
            [0, 3, 0, 5],
            [6, 8, 5, 0]]


def prim(graph: List[List[int]]) -> int:
    included = [0] * len(graph[0])
    totalCost = 0

    currentNode = 0
    while included.count(1) < len(thegraph[0]):
        minCost = 999
        for i in range(len(thegraph[0])):
            if graph[currentNode][i] < minCost and included[i] != 1:
                totalCost += graph[currentNode][i]
                included[i] = 1
                currentNode = i
    return totalCost


minimumCost = prim(thegraph)
print(minimumCost)
