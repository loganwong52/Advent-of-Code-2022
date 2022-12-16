def getYourPoints(you):
    if you == 'X':
        # lose
        return 0
    elif you == 'Y':
        #  draw
        return 3
    else:
        # win
        return 6


def getScore(opponent, you):
    score = 0
    score += getYourPoints(you)

    # Opponent is rock
    if opponent == 'A':
        if you == 'X':
            # lose. scissors
            score += 3
        elif you == 'Y':
            #  draw. rock
            score += 1
        else:
            # win. paper
            score += 2

    elif opponent == 'B':
        # Opponent is Paper
        if you == 'X':
            # you lose. rock
            score += 1
        elif you == 'Y':
            #  you draw. paper
            score += 2
        else:
            # you win. scissors
            score += 3
    else:
        # opponent is Scissors
        if you == 'X':
            # you lose. paper
            score += 2
        elif you == 'Y':
            #  you draw. scissors
            score += 3
        else:
            # you win. rock
            score += 1

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
