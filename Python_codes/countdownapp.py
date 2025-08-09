import datetime

userInput=input("enter your goal with deadline....separated by colon\n")
inputList=userInput.split(":")

goal=inputList[0]
deadline=inputList[1]

print(datetime.datetime.strptime(deadline,"%d.%m.%Y"))
print(type(datetime.datetime.strptime(deadline,"%d.%m.%Y")))

#user input will always be treated as string
#learn python:12.07.2025



