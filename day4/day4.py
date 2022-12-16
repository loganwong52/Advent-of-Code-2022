def has_overlap(assignment0, assignment1):
    first = assignment0[0]
    second = assignment0[1]
    third = assignment1[0]
    fourth = assignment1[1]
    # print(first)
    # print(second)
    # print(third)
    # print(fourth)

    #  check if first is between third and fourth
    if third <= first and first <= fourth and third <= second and second <= fourth:
        # check if second is between third and fourth
        return True

    # check if third is between first and second
    elif first <= third and third <= second and first <= fourth and fourth <= second:
        # check if fourth is also between first and second
        return True

    # if first and second are the same
    elif first == second and third <= first and first <= fourth:
        # check if they fall between third and fourth
        return True

    # if third and fourth are the same
    elif third == fourth and first <= third and third <= second:
        # check if they fall between first and second
        return True

    # check if they're all the same
    elif first == second and first == third and first == fourth:
        return True

    return False


total_overlap = 0
f = open('data.txt', 'r')
foo = f.readlines()
for i in range(0, len(foo)):
    line = foo[i]
    line = line.strip('\n')
    assignments = line.split(",")
    assignments[0] = assignments[0].split("-")
    assignments[0][0] = int(assignments[0][0])
    assignments[0][1] = int(assignments[0][1])

    assignments[1] = assignments[1].split("-")
    assignments[1][0] = int(assignments[1][0])
    assignments[1][1] = int(assignments[1][1])
    # print(assignments)

    overlaps = has_overlap(assignments[0], assignments[1])
    # print(overlaps)

    if overlaps:
        total_overlap += 1

print(total_overlap)
# 602
