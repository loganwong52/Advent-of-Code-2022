
def findMatch(first, second):
    for letter in first:
        if letter in second:
            return letter


def checkMath(matchingLetter, number, letterToCheck):
    if matchingLetter is letterToCheck:
        print(matchingLetter, ":  ", number)


total = 0
with open('data.txt') as openFile:
    for line in openFile:
        line = line.strip('\n')
        # print(len(line))
        halfway_index = len(line)//2 - 1
        # print(halfway_index)
        first = line[0:halfway_index + 1]
        second = line[halfway_index + 1:]
        # print(first, "   ", second)

        match = findMatch(first, second)
        number = ord(match)
        if match.islower():
            number -= 96
            # print(number)
        else:
            number -= 38
            # print(number)

        # checkMath(match, number, "P")
        total += number

    print(total)


# A   B  C  D  E  F G
# 27 28 29 30 31 32 33
