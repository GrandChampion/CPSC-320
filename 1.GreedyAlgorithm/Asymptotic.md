# Asymptotic analysis

## O(1)
- Most efficient algorithm
```python
# list operations
list = [1,2,3]
list[0] # list access
list.append(4)
```
```python
# Hashmap, set operations
theHashMap = {}
theHashMap["k1"] = 1 #insert
theHashMap["k1"] # access
```
---
## O(log n)
- reduce array in half every iteration
```python
# Binary search
```
```python
# push and pop from heap
```
---
## O(sqrt(n))
```python
# getting factors
```
---
## O(n)
- As input size grow, complexity grows proportionally
```python
# iteration
for i in range(5):
    print(n)

while j < n:
    print(j)
    j+=1
```
```python
# Insert in the middle of a list
list.insert(3,'h')

# Remove item in the list which is not the beginning or end
list.remove('h')
# search in list
list.index('h')
```
```python
# Building heap
heapq.heapify(n)
```
---
## O(n^2)
```python
# Iterating 2D matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
```
---
## O(nm)
```python
# Iterating through n x m matrix
```
---
## O(n log n)
```python
Merge sort
```
```python
Heap sort
```
---
## O(n^3)
```python
# Iterating through 3D matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for k in range(len(matrix[i][j])):
            print(matrix[i][j][k])
```
---
## O(2^n)
```python
# Recursion
def recursion(i, n):
    if i == len(n):
        return 0
    else:
        branch1 = recursion(i+1,n)
        branch2 = recursion(i+2, n)
```
---
## O(n!)
```python
# Permutation
# Travelling Salesman Problem
```
---