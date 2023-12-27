employeeIntervals = [[8, 10], [6, 12], [22, 30], [31, 55], [7, 8]]


def performerIntervals(employeeSchedule):
    employeeSchedule = sorted(employeeSchedule, key=lambda x: x[1])
    covered = [0]*len(employeeIntervals)

    performerShifts = []
    for i in range(len(employeeSchedule)):
        if covered[i] == 0:
            newPerformerShift = [employeeSchedule[i]
                                 [1], employeeSchedule[i][1]+1]
            performerShifts.append(newPerformerShift)
            covered[i] = 1
            for j in range(len(employeeSchedule)):
                if i == j:
                    continue
                else:
                    if newPerformerShift[0] >= employeeSchedule[j][0]:
                        covered[j] = 1
    return performerShifts


print(performerIntervals(employeeIntervals))
