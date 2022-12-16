def getYourPoints(you):
    if you == 'X':
        # rock
        return 1
    elif you == 'Y':
        #  paper
        return 2
    else:
        # scissors
        return 3


def getScore(opponent, you):
    score = 0
    score += getYourPoints(you)

    # Opponent is rock
    if opponent == 'A':
        if you == 'X':
            # draw
            score += 3
        elif you == 'Y':
            #  you win
            score += 6
        else:
            # you lose
            score += 0
    elif opponent == 'B':
        # Opponent is Paper
        if you == 'X':
            # you lose
            score += 0
        elif you == 'Y':
            #  you draw
            score += 3
        else:
            # you win
            score += 6
    else:
        # opponent is Scissors
        if you == 'X':
            # you win
            score += 6
        elif you == 'Y':
            #  you lose
            score += 0
        else:
            # draw
            score += 3

    return score


totalScore = 0
i = 1
with open('rps.txt') as openFile:
    for line in openFile:
        line = line.strip("\n")
        moves = line.split(" ")

        # print("opponent: ", moves[0])
        # print("you: ", moves[1])

        pointsYouWon = getScore(moves[0], moves[1])
        totalScore += pointsYouWon
        # print(i, ".   ", pointsYouWon)
        i += 1

print("TOTAL SCORE: ", totalScore)
