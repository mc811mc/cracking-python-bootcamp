from random import randint

#user input for unlimited or number of chances
answer = randint(1, 100)
tries = randint(1, 10)
attempt = 0
summation = 0
choice = 0

#program start
mode = str(input("Do you want unlimited tries? Enter 'y' for yes and 'n' for no. Your choice: "))
mode = mode.lower()
if mode == "y":
    while choice != answer:
        choice = int(input("Enter a number in the range of 1-100. Your number: "))
        if choice < 1 or choice > 100:
            print("Invalid input: Must enter within the range of 1-100")
            exit()
        else:
            attempt += 1
            summation += choice
            if choice < min:
                min = choice
            if choice > max:
                max = choice
            if choice < answer:
                print(choice, "is less than the secret number.")
            elif choice > answer:
                print(choice, "is bigger than the secret number")
            elif choice == answer:
                print(choice, "is the correct answer. You win!")
elif mode == "n":
    print("Total Tries:", tries)
    for x in range(tries):
        if tries != 0:
            choice = int(input("Enter a number in the range of 1-100. Your number: "))
            if choice < 1 or choice > 100:
                print("Invalid input: Must enter within the range of 1-100")
                exit()
            attempt += 1
            summation += choice
            tries -= 1
            if choice < min:
                min = choice
            if choice > max:
                max = choice
            if choice < answer:
                print(choice, "is less than the secret number.")
                if tries != 0:
                    print("You have", tries, "tries left!")
            elif choice > answer:
                print(choice, "is bigger than the secret number")
                if tries != 0:
                    print("You have", tries, "tries left!")
            elif choice == answer:
                print(choice, "is the correct answer. You win!")
                break
else:
    print()
    print("Invalid input, goodbye")
    exit()

#scoresheet
print("Number of tries:", attempt)
print("Max number you guessed:", max)
print("Min number you guessed:", min)
print("Summation of the numbers:", summation)
print("The average of the numbers:", summation/attempt)
