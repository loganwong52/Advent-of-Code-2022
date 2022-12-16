def getTopOfAllStacks():
    for i in range(1, 10):
        print(all_stacks.get(i)[-1], end="")
    print("")


f = open('data.txt', 'r')
the_file = f.readlines()


stack1 = ['B', 'G', 'S', 'C']
stack2 = ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G']
stack3 = ['M', 'Q', 'S']
stack4 = ['B', 'S', 'L', 'T', 'W', 'N', 'M']
stack5 = ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P']
stack6 = ['C', 'T', 'B', 'G', 'Q', 'H', 'S']
stack7 = ['T', 'J', 'P', 'B', 'W']
stack8 = ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M']
stack9 = ['N', 'S', 'H', 'B', 'P', 'F']

all_stacks = {
    1: stack1,
    2: stack2,
    3: stack3,
    4: stack4,
    5: stack5,
    6: stack6,
    7: stack7,
    8: stack8,
    9: stack9
}


for line in the_file:
    line = line.replace("move", "")
    line = line.replace("from", "")
    line = line.replace("to", "")
    line = line.strip("\n")
    input = line.split(" ")

    # print(input)
    amount = int(input[1])
    start_location = int(input[3])
    end_location = int(input[5])

    # print(amount, " ", start_location, " ", end_location)
    start_stack = all_stacks.get(start_location)
    end_stack = all_stacks.get(end_location)

    if amount == 1:
        element_removed = start_stack.pop()
        end_stack.append(element_removed)
    else:
        # print("start_stack: ", start_stack)
        elements_removed = start_stack[len(start_stack) - amount:]
        end_stack += elements_removed
        # print("end_stack: ", end_stack)
        for i in range(0, amount):
            start_stack.pop()
        # print("new start_stack: ", start_stack)


getTopOfAllStacks()
