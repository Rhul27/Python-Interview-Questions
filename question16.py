# Menu Driven Program
flag=True
while flag:
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))
    print(
        '''
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        '''
    )
    choice=int(input("Enter your Choice : "))

    if choice==1:
        print("Addition : ",num1+num2)
    elif choice==2:
        print("Subtraction : ",num1-num2)
    elif choice==3:
        print("Multiplication : ",num1*num2)
    elif choice==4:
        print("Division : ",num1/num2)
    else:
        print("You have enterd wrong choice ")
    a=input("Do u want to contiune y/n : ")
    if a=="n":
        flag=False
    elif a=="y":
        flag=True
    else:
        print("You entered wrong choice")
        a=input("Do u want to contiune y/n : ")
