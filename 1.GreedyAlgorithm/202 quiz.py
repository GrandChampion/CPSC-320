givenDelays = [[1, 1], [2, 4], [3, 8]]
theTasks = [2, 1, 1, 2, 3]

# represent the accumulated delay
# each index represent delay of task 1, 2, 3
d = [0]*len(givenDelays)

days = [0] * len(theTasks)


def dayFinder(delays, tasks):

    for i in range(len(tasks)):
        if i == 0:
            days[0] = 1
            d[tasks[0]-1] += delays[tasks[0]-1][1]
            continue
        else:
            if tasks[i-1] == tasks[i]:
                days[i] = (days[i-1] + 1) + d[tasks[i]-1]
            else:
                days[i] = (days[i-1] + 1) + d[tasks[i]-1]
            daysAdded = 1+d[tasks[i]-1]
            # day passed
            for j in range(len(d)):
                if d[j] > 0:
                    d[j] -= daysAdded
            d[tasks[i]-1] += delays[tasks[i]-1][1]

    return days


print(dayFinder(givenDelays, theTasks))
