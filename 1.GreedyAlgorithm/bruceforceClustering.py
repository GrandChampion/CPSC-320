# Nodes are numbered from 0 to n-1
# There are 2 category

instance1 = [1, 2, 1, 2, 1]
similarityMatrix1 = [[0, 2, 7, 3, 5],
                     [2, 0, 9, 2, 1],
                     [7, 9, 0, 7, 9],
                     [3, 2, 7, 0, 4],
                     [5, 1, 9, 4, 0]]


def costChecker(instance, similarityMatrix):
    cost = 0  # initially, set it to 0
    for i in range(len(instance)):
        for j in range(len(instance)):
            # Finding maximum similarity, which is the cost of clustering
            if (instance[i] != instance[j] and cost < similarityMatrix[i][j]):
                cost = similarityMatrix[i][j]
    return cost


costBetweenTwoCategories = costChecker(instance1, similarityMatrix1)
print(costBetweenTwoCategories)
