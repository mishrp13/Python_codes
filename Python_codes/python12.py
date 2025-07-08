# simple Cli calculator


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def calculator():
    print("simple calculator: ")
    print("___________________")
    print("select operations: ")
    print("1. Add")
    print("2. sub")
    print("3. mul")
    print("4. Div")


    choice=input("enter the choice between 1,2,3,4: ")

    if choice not in ('1','2','3','4'):
        print("Invalid choice")
        return
    
    try:
        num1=float(input("enter the first number: "))
        num2=float(input("enter the second number: "))
    except ValueError:
        print("Invalid input: , enter numbers only")
        return
    

    if choice == '1':
        print("Result: ", add(num1,num2))
    elif choice == '2':
        print("Result: ", sub(num1,num2))
    elif choice == '3':
        print("Result", mul(num1,num2))
    elif choice== '4':
        print("Result", div(num1,num2))


if __name__=="__main__":
    calculator()
