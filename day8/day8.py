

f = open('data.txt', 'r')
the_file = f.readlines()

# add the left and right edges together
# 99 rows
visible_trees = len(the_file) * 2  # 198

# add the top and bottom trees, minus the 4 corners
# 100 columns
topAndBottom = len(the_file[0]) * 2
topAndBottom -= 4
visible_trees += topAndBottom

print(visible_trees)  # 394


for row in range(1, len(the_file) - 1):
    line = the_file[row]
    line = line.strip("\n")

    left = the_file[row][0]
    right = the_file[row][len(line) - 1]

    print("LEFT: ", left)
    print("RIGHT: ", right)
    for col in range(1, len(line) - 1):
        top = the_file[0][col]
        bottom = the_file[len(the_file) - 1][col]

        print("TOP: ", top)
        print("BOTTOM: ", bottom)

        # get the current tree
        number = int(line[col])

        # check up

        # check left

        # check right

        # check down

        break
        # print(number, end="")
    # print("")
    # break
