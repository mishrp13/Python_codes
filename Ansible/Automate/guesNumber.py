import random

print("Hello, what is your name?. ")
name=input()

print("well "+ name + "I am thinking of number between 1 and 20")
secretNumber=random.randint(1,20)

print("Debug:"+ str(secretNumber))

for guesstaken in range(1,7):
    print("Take a guess")
    guess=int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    else:
        break

if guess == secretNumber:
    print("Good job " + name + " you guessed my number in "+ str(guesstaken))
else:
    print("Nope. The number i was thinking "+str(secretNumber))