from collections import Counter
# Each nodes are numbered 0, 1, 2, 3

# Tuple edge = (node1, node2, similarity)
edges1 = [(0, 1, 5), (0, 3, 2), (1, 2, 7), (2, 3, 1)]

# algorithm to group into two
def greedyClustering(edges):
    # sort edges in decreasing order based on similarity
    edges = sorted(edges, key=lambda x: x[2], reverse=True)
    print(edges)

    # put each node in each categories
    # number represent which category node is belongs to.
    category = [0, 1, 2, 3]
    goalCategories = 2

    i = 0

    # len(Counter(edges).keys()) represents number of types of categories
    while len(Counter(category).keys()) > goalCategories:
        # if node1 and node2 belong to different category
        if (category[edges[i][0]] != category[edges[i][1]]):
            category[edges[i][1]] = 0
            category[edges[i][0]] = 0
        i += 1
    return category


print(greedyClustering(edges1))
