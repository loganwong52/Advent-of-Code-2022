
allSums = []

localTotal = 0
with open('numbers.txt') as openFile:
    for line in openFile:
        if (line == '\n'):
            allSums.append(localTotal)
            localTotal = 0
        else:
            numericLine = int(line)
            localTotal += numericLine


allSums.sort(reverse=True)
print(allSums[0])
print(allSums[1])
print(allSums[2])


# PUZZLE 2:
topThree = allSums[0] + allSums[1] + allSums[2]
print("TOTAL: ", topThree)
