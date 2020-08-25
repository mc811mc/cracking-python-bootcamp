from random import randint
from time import sleep

a = randint(0,9)
b = randint(0,9)
c = randint(0,9)
d = randint(0,9)

win = [a,b,c,d]

lottery = int(input("Which Daily would you like to play? Daily "))
if lottery == 3:
    guess_a = int(input("What is your first number - "))
    sleep(2)
    if a == guess_a:
        pass
    else:
        print("You have lost the lottery.")
        print("The winning numbers were " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + '.')
        exit()
    guess_b = int(input("What is your second number - "))
    sleep(2)
    if b == guess_b:
        pass
    else:
        print("You have lost the lottery.")
        print("The winning numbers were " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + '.')
        exit()
    guess_c = int(input("What is your third number - "))
    sleep(2)
    if c == guess_c:
        print("The winning numbers are " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + '.')
        print("You have won the lottery!")
    else:
        print("You have lost the lottery.")
        print("The winning numbers were " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + '.')
        exit()
elif lottery == 4:
    guess_a = int(input("What is your first number - "))
    sleep(2)
    if a == guess_a:
        pass
    else:
        print("You have lost the lottery.")
        print("The winning numbers were " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + ', and ' + str(win[3]) + '.')
        exit()
    guess_b = int(input("What is your second number - "))
    sleep(2)
    if b == guess_b:
        pass
    else:
        print("You have lost the lottery.")
        print("The winning numbers were " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + ', and ' + str(win[3]) + '.')
        exit()
    guess_c = int(input("What is your third number - "))
    sleep(2)
    if c == guess_c:
        pass
    else:
        print("You have lost the lottery.")
        print("The winning numbers were " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + ', and ' + str(win[3]) + '.')
        exit()
    guess_d = int(input("What is your fourth number - "))
    sleep(2)
    if d == guess_d:
        print("The winning numbers are " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + ', and ' + str(win[3]) + '.')
        print("You have won the lottery!")
    else:
        print("You have lost the lottery.")
        print("The winning numbers were " + str(win[0]) + ', ' + str(win[1])  + ', ' + str(win[2]) + ', and ' + str(win[3]) + '.')
        exit()
else:
    print("You chose to play neither Daily 3 or 4. Restarting...")
    exit()