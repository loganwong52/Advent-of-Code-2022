
def findMatch(line1, line2, line3):
    shortestLen = min(len(line3), min(len(line1), len(line2)))

    shortest = ""
    other1 = ""
    other2 = ""
    if len(line1) is shortestLen:
        shortest = line1
        other1 = line2
        other2 = line3
    elif len(line2) is shortestLen:
        shortest = line2
        other1 = line1
        other2 = line3
    else:
        shortest = line3
        other1 = line1
        other2 = line2

    for letter in shortest:
        if letter in other1 and letter in other2:
            return letter


def checkMath(matchingLetter, number, letterToCheck):
    if matchingLetter is letterToCheck:
        print(matchingLetter, ":  ", number)


total = 0
f = open('data.txt', 'r')
foo = f.readlines()
total = 0
for i in range(0, len(foo), 3):
    line1 = foo[i].strip('\n')
    line2 = foo[i + 1].strip('\n')
    line3 = foo[i + 2].strip('\n')

    # print(line1)
    # print(line2)
    # print(line3)
    # print("")

    badge = findMatch(line1, line2, line3)
    # print(badge)

    number = ord(badge)
    if badge.islower():
        number -= 96
        # print(number)
    else:
        number -= 38
        # print(number)

    # checkMath(badge, number, "Z")
    total += number

print(total)

# A   B  C  D  E  F G
# 27 28 29 30 31 32 33
