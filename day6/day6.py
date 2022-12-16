f = open('data.txt', 'r')
the_file = f.readlines()

input = the_file[0]

# print(len(input))

for i in range(0, len(input) - 3):
    test = input[i:i+4]
    # print(test)
    if test[0] != test[1] and test[0] != test[2] and test[0] != test[3] and test[1] != test[2] and test[1] != test[3] and test[2] != test[3]:
        print(test)
        print(i)
        # add 3, plus 1, so add 4 from i
        print(i + 4)
        break
