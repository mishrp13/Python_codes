print("how many cats do you have")
numcats=input()

try:
    if int(numcats) >=4:
        print("You have too many cats")
    else:
        print("You don't have too many cats")
except ValueError:
    print("you did not enter a number")

