from random import randint
from time import sleep

#counters
win, lose = 0, 0

dice_numbers = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}

#input of how many games the user is going to play
rounds = int(input("How many rounds you want to play? Enter a number from 1-20: "))
if rounds < 0 or rounds > 20:
    print()
    print("Invalid input. Exiting program...")
    exit()
print()
print("Rounds to Play - ", rounds)
print()
while rounds >= 1:
    roll = int(input("Roll the dice. Enter a number from 1-6... "))
    if roll <= 0 or roll >= 7:
        print()
        print("Invalid input. Exiting program...")
        exit()
    #if roll >= 1:
    print()
    print("Dice Rolling... \n")
    dice_result = randint(1, 6)
    # counter updates
    if dice_result == 1:
        dice_numbers[1] += 1
    elif dice_result == 2:
        dice_numbers[2] += 1
    elif dice_result == 3:
        dice_numbers[3] += 1
    elif dice_result == 4:
        dice_numbers[4] += 1
    elif dice_result == 5:
        dice_numbers[5] += 1
    elif dice_result == 6:
        dice_numbers[6] += 1
    #result delay
    sleep(3)
    rounds -= 1
    if roll == dice_result:
        win += 1
        print("You win! The dice landed on", dice_result, "\n")
    elif roll != dice_result:
        lose += 1
        print("Better luck next time. Dice landed on", dice_result, "\n")
print("You are out of tries. The results will be printed out shortly. \n")
sleep(2)
print("Dice landed on 1:", dice_numbers[1], "times \n")
print("Dice landed on 2:", dice_numbers[2], "times \n")
print("Dice landed on 3:", dice_numbers[3], "times \n")
print("Dice landed on 4:", dice_numbers[4], "times \n")
print("Dice landed on 5:", dice_numbers[5], "times \n")
print("Dice landed on 6:", dice_numbers[6], "times \n")
print("Wins: ", win, "\n")
percent = (win / (win + lose) * 100)
print("Winning Percentage: ", percent, '%')




