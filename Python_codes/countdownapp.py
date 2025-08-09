import datetime

userInput=input("enter your goal with deadline....separated by colon\n")
inputList=userInput.split(":")

goal=inputList[0]
deadline=inputList[1]

# print(datetime.datetime.strptime(deadline,"%d.%m.%Y"))
# print(type(datetime.datetime.strptime(deadline,"%d.%m.%Y")))

deadline_date=datetime.datetime.strptime(deadline,"%d.%m.%Y")
today_date=datetime.datetime.today()


#user input will always be treated as string
#learn python:12.10.2025

# calculate how many days from now till deadline

print(deadline_date-today_date)




