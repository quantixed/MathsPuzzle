#! /usr/bin/env python
import random, time

#welcome message and get the user's name
print("Welcome to the multiplication game.")
print("What's your name?")
name = input("Name: ")
print("OK,", name, "you will do 5 tests.")
print("Each test will be ten questions and you will have 1 minute for each!")
bank = 0
qright = 0

for game in range(0,5):
    readystr = ""
    while len(readystr) == 0:
        readystr = input("Ready?")
    start = time.time()

    for num in range(0,10):
        #set up each question
        number1 = random.randint(2,12)
        number2 = random.randint(2,12)
        answer = number1 * number2

        guess = 0
        print("What is", number1, "x", number2, "?")

        while guess != answer:
            guess = int(input("Answer: "))
            if guess != answer:
                print("  No, try again")

        curr = time.time()
        timeleft = (60 + bank) - (curr - start)
        if (timeleft > 0):
            print("  CORRECT!", "You have", int(timeleft), "seconds left.")
            qright = qright + 1
        else:
            print("  TIME'S UP! Sorry!")
            break

    if (game + 1) * 10 == qright:
        bank = timeleft
        print("That was test", game + 1)
        if (game + 1 < 5):
            print(name, "YOU DID IT! Now onto test", game + 2)
        else:
            print(name, "YOU DID IT! That was amazing! You win!")
    else:
        print("Please try again.")
        break
print("G A M E  O V E R")
