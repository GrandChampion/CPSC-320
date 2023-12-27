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
print(greedyResult)
