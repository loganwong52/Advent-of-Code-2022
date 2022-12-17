f = open('data.txt', 'r')
the_file = f.readlines()

root = {
    "/": None
}

current_dir_name = "/"
current_dir = root

for line in the_file:
    if line[0] == "$":
        # print(line)
        if line[2:4] == "cd":
            print(line)
            directory_to_change_into = line[6:]
            directory_to_change_into = directory_to_change_into.strip("\n")
            current_dir_name = directory_to_change_into

        elif line[2:4] == "ls":
            root[current_dir_name] = {}
    else:
        if line[0:3] == "dir":
            print(line)
