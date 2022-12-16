def has_overlap(assignment0, assignment1):
    first = assignment0[0]
    second = assignment0[1]
    third = assignment1[0]
    fourth = assignment1[1]
    # print(first)
    # print(second)
    # print(third)
    # print(fourth)

    x = range(first, second)
    y = range(third, fourth)

    # print(x)
    # print(y)

    big_x = max(first, third)
    small_y = min(second, fourth)+1

    # print(big_x)
    # print(small_y)
    numbers_in_common = range(big_x, small_y)
    # print("numbers in common: ", numbers_in_common)

    if len(numbers_in_common) > 0:
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
    print(overlaps)

    if overlaps:
        total_overlap += 1

print(total_overlap)
