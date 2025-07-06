
# Create a function that accepts two numbers and returns the larger.


a =int(input("enter any number: "))
b= int(input("enter any number: "))


def get_larger_number(a,b):
    if a>b:
        return a
    else:
        return b
    
result=get_larger_number(a,b)
print(f"The largest number is: {result}")





