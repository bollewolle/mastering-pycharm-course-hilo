""" Part of Excercise: https://github.com/bollewolle/mastering-pycharm-course/tree/master/your-turn/3-source-control"""
import random

print("Welcome to the Hi-Lo game")
num = random.randint(1, 100)
guess = 0

while guess != num:
    guess = int(input("Guess a number between 1 & 100: "))
    if guess == num:
        print("Got it: The number is {}".format(guess))
        break
    elif guess < num:
        print("Too low!")
        continue
    elif guess > num:
        print("Too high!")
        continue
