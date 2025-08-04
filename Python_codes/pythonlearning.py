
# 1st program

# print("Hello,World")
# print("what's your name")

# myName=input()
# print("It is good to meet you "+ myName)
# print("The length of your name is")
# print(len(myName))
# print("what's your age")
# myAge=input()
# print("you will be "+str(int(myAge)+20)+ " in 20 years down the line and that is not absurd")


# file_path="destination.txt"
# open_file=open(file_path,'r')
# text=open_file.read()
# print(open_file)
# open_file.close()

file_path="destination.txt"
# open_file=open(file_path,'r')
# text=open_file.readlines()
# print(text)

with open(file_path,'r') as open_file:
    text=open_file.readlines()

print(text)


