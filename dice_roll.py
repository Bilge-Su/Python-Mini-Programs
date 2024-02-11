import random

diceRollList = []
i = 0

while i < 6:

    question = input("Do you wanna roll the dice? ")
    if question.lower() != "yes": break
    else:
        diceRoll = random.randint(1, 6)
        print("You got " + str(diceRoll))
        diceRollList.append(str(diceRoll))
        i += 1

print(diceRollList)