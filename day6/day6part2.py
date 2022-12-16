f = open('data.txt', 'r')
the_file = f.readlines()

input = the_file[0]

# print(len(input))

for i in range(0, len(input) - 13):
    test_packet = input[i:i+14]

    # create an empty dictionary to store the letter counts
    letter_counts = {}

    # iterate through each letter in the string
    for letter in test_packet:
        # if the letter is not in the dictionary, add it and set the count to 1
        if letter not in letter_counts:
            letter_counts[letter] = 1
        # if the letter is already in the dictionary, increment the count
        else:
            letter_counts[letter] += 1

    values = letter_counts.values()

    # check if all values in the list are equal
    result = all(x == 1 for x in values)

    # print the result
    # print(result)
    if result:
        print(test_packet)
        print(i)
        print(i + 14)
        break
