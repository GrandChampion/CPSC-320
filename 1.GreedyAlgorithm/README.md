# Greedy algorithm
## Chracteristics
- Make optimal choice at each iteration, not considering the future and the past interations
- Greedy solution not always make optimal solution

## Examples

### 1 (Machine Learning) Clustering from worksheet
#### 1.1 Brute force
##### 1.1.1 Making instances
```python
# Each Instance[i] represent which category that node belongs to.
instance26 = [1, 2, 1, 2, 1]
# Total instances = 2^nodes
```
##### 1.1.2 Checking each instances if it is optimal
```python
def costChecker(instance, similarityMatrix):
    cost = 0  # initially, set it to 0
    for i in range(len(instance)):
        for j in range(len(instance)):
            # Finding maximum similarity, which is the cost of clustering
            if (instance[i] != instance[j] and cost < similarityMatrix[i][j]):
                cost = similarityMatrix[i][j]
    return cost
```
#### 1.2 Greedy clustering
- Strategy
  - 1. put each edges into its own category
  - 2. pick edges that have highest similarity and combine the category
  - 3. do 1 and 2 until it reaches intended category numbers
```python
def greedyClustering(edges):
    # sort edges in decreasing order based on similarity
    edges = sorted(edges, key=lambda x: x[2], reverse=True)
    print(edges)

    # put each node in each categories
    # number represent which category node is belongs to.
    category = [0, 1, 2, 3]
    goalCategories = 2

    i = 0

    # len(Counter(edges).keys()) represents number of unique elements in the list
    while len(Counter(category).keys()) > goalCategories:
        # if node1 and node2 belong to different category
        if (category[edges[i][0]] != category[edges[i][1]]):
            category[edges[i][1]] = 0
            category[edges[i][0]] = 0
        i += 1
    return category
```

### 2. MST
definition: subset of edges from the graph that connect all vertices without cycle and with minimum total edge cost.
#### 1.1 Kruskal(Russian)'s algorithm
- Strategy
  - 1. sort the edges in ascending order of weight
  - 2. pick smallest weighted edge and check if it forms cycle
  - 3. If it doesn't form the cycle, include it in the MST
  - 4. iterate 2 and 3 until 
```pseudocode
def kruskal(graph, weight list):
    A = []
    for each vertex in graph:
        put it into single list like [[0],[1],[2],[3]]
    edges = list of edges
    sort edges in ascending order of weight

    for e of edges:
        if adding e does not create cycle:
            A.append(e)
    return A
```
#### 1.2 Prim(French)'s algorithm
- Strategy
  - 1. pick a random node in the beginning
  - 2. check edges that connects from visited nodes to not yet reached nodes
  - 3. pick the smallest weight edge among them
  - 4. iterate 2 and 4 until it includes all nodes in the graph
```python
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
```
### 3. Knapsack problem
```python
weight1 = [(1/2, 3), (1/2, 1), (1/2, 7), (1/2, 4)]
weight2 = [(1/4, 1), (1/4, 6), (1/4, 7), (1/4, 5)]
weight3 = [(1/8, 9), (1/8, 4), (1/8, 3), (1/8, 7)]
weight4 = [(1/16, 4), (1/16, 4), (1/16, 8), (1/16, 2)]

# Sort weight4 based on value
weight4 = sorted(weight4, key=lambda x: x[1], reverse=True)
tuple1 = (1/8, weight4[0][1]+weight4[1][1])
tuple2 = (1/8, weight4[2][1]+weight4[3][1])
weight3.append(tuple1)
weight3.append(tuple2)

weight3 = sorted(weight3, key=lambda x: x[1], reverse=True)
tuple1 = (1/4, weight3[0][1]+weight3[1][1])
tuple2 = (1/4, weight3[2][1]+weight3[3][1])
tuple3 = (1/4, weight3[4][1]+weight3[5][1])
weight2.append(tuple1)
weight2.append(tuple2)
weight2.append(tuple3)

weight2 = sorted(weight2, key=lambda x: x[1], reverse=True)
tuple1 = (1/2, weight2[0][1]+weight2[1][1])
tuple2 = (1/2, weight2[2][1]+weight2[3][1])
tuple3 = (1/2, weight2[4][1]+weight2[5][1])

weight1.append(tuple1)
weight1.append(tuple2)
weight1.append(tuple3)

weight1 = sorted(weight1, key=lambda x: x[1], reverse=True)

greedyResult = weight1[0][1]+weight1[1][1]
```
### 4. Interval scheduling
#### 4.1 Check non of intervals are overlapping
```python
def overlapChecker(intervals: List[List[int]]) -> bool:
    if len(intervals) == 0:
        return True
    else:
        # sort by starting time of each intervals
        intervals.sort(key=lambda x: x[0])
        previousEnd = intervals[0][1]
        for interval in intervals[1:]:
            # Check if previous interval's end time and current interval's start time don't overlap
            if previousEnd <= interval[0]:
                previousEnd = interval[1]
            else:
                return False
        return True
```
#### 4.2 Minimum number of rooms that can accomodate all of intervals
```python
def requiredRooms(intervals: List[List[int]]) -> int:
    startTime = [i[0] for i in intervals]
    startTime = sorted(startTime)

    endTime = [i[1] for i in intervals]
    endTime = sorted(endTime)

    maxRequired = 0
    currentRequired = 0

    curStartTimeIndex = 0
    curEndTimeIndex = 0

    while curStartTimeIndex < len(intervals):
        if endTime[curEndTimeIndex] > startTime[curStartTimeIndex]:
            curStartTimeIndex += 1
            currentRequired += 1
        else:
            curEndTimeIndex += 1
            currentRequired -= 1
        maxRequired = max(maxRequired, currentRequired)

    return maxRequired
```
#### 4.3 Count minimum number of intervals that overlap
```python
def removeOverlappingIntervals(intervals: List[List[int]]) -> int:
    removed = 0
    selectedEndTime = intervals[0][1]

    # Sanity check: sort based on start time
    sorted(intervals, key=lambda x: x[0])

    for interval in intervals[1:]:
        if interval[0] < selectedEndTime:
            # remove overlapping interval that ends late
            removed += 1
            selectedEndTime = min(selectedEndTime, interval[1])
        else:
            # nothing to remove
            selectedEndTime = interval[1]
    return removed
```

## Proof technique
### 1. Stays Ahead
- 1. Define
  - A: solution from greedy algorithm
  - O: solution from optimal algorithm
- 2. list each iteration of both greedy algorithm and optimal algorithm

  |$ a_k $|$o_k$|Comparison|
  |---|---|---|
  | 3  |  2 |$a_1>o_1$|
  | 4  |  3 |$a_2>o_2$|
  |  5 |  4 |$a_3>o_3$|
- 3. As greedy solution in each iteration stays ahead, greedy solution is the optimal solution.
### 2. An Exchange Argument
- 1. Define results got from greedy algorithm and optimal algorithm
  - $A=\{a_1,a_2,a_3,\cdots,a_k\}$
  - $O=\{o_1,o_2,o_3,\cdots,o_k\}$
- 2. Find elements that are different between A and O
  - case1: element in optimal solution does not exist in greedy solution. $o_*$ is not in $A$.
  - case2: order is different. $\{a_2,a_3\}=\{o_3,o_2\}$
- 3. Modify optimal solution $O$ to match $A$
  - case1: delete value that is only in optimal solution. delete $o_*$.
  - case2: change the order of optimal solution to match greedy solution. $\{o_3\leftrightarrow o_2\}$
- 4. If modified optimal solution doesn't get worse than original version, then greedy solution is as good as optimal solution.